from sqlalchemy.orm import Session
from app.api.models.ft_user.User import User
from app.api.models.ft_user_address.UserAddress import UserAddress
from app.api.models.ft_user_info.UserInfo import UserInfo
from app.api.models.ft_processed_item.ProcessedItem import ProcessedItem
from app.api.models.ft_payment_method.PaymentMethod import PaymentMethod
from app.api.models.ft_payment_address.PaymentAddress import PaymentAddress
from app.api.models.ft_subscription.Subscription import Subscription
from app.api.models.ft_payment_history.PaymentHistory import PaymentHistory
from app.api.utils.tokenHandler import decode_jwt

async def get_user_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()

async def get_user_by_token(token: str, db: Session):
    payload = decode_jwt(token)
    user = await get_user_by_email(payload['email'], db)
    user.password = None
    return user

async def get_user_info_address(email: str, db: Session):
    user = (
        db.query(User)
        .join(UserInfo, User.id == UserInfo.user_id)
        .join(UserAddress, User.id == UserAddress.user_id)
        .filter(User.email == email)
        .first()
    )
    user.password = None
    return user

async def get_all_active_users(db: Session):
    users = (db.query(User)
        .join(User.user_info)
        .join(User.user_address)
        .join(User.processed_item)
        .join(User.payment_method)
        .join(User.payment_address)
        .join(User.subscription)
        .join(User.payment_history)
        .filter(User.deleted_at.is_(None))
        .all())
    for user in users:
        user.password = None
    return users
