"""
Nome do arquivo: authRoute.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 15/01/2024
Descrição: Arquivo responsável pela rota de usuários.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from app.api.models.ft_user.User import User
from app.api.models.ft_user_address.UserAddress import UserAddress
from app.api.models.ft_user_info.UserInfo import UserInfo
from app.api.models.ft_processed_item.ProcessedItem import ProcessedItem
from app.api.models.ft_payment_method.PaymentMethod import PaymentMethod
from app.api.models.ft_payment_address.PaymentAddress import PaymentAddress
from app.api.models.ft_subscription.Subscription import Subscription
from app.api.models.ft_payment_history.PaymentHistory import PaymentHistory
from sqlalchemy.orm import Session
from app.api.utils.tokenAuth import TokenAuth
from app.db.sqlalchemy import get_db

users_router = APIRouter(prefix="/users")

@users_router.get('/{email}')
async def findOne(email: str, db: Session = Depends(get_db)):
    try:
        user = (
            db.query(User)
            .join(UserInfo, User.id == UserInfo.user_id)
            .join(UserAddress, User.id == UserAddress.user_id)
            .filter(User.email == email)
            .first()
        )

        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        user.password = None

        data_response = {
            'msg':'Usuário encontrado',
            'data':{
                'user': user
            }
        }
        
        return data_response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f'Erro inesperado, tente novamente.\nDescrição: {e}')


@users_router.get('/',  dependencies=[Depends(TokenAuth())])
async def findAll(db: Session = Depends(get_db)):
    try:
        result = (db.query(User)
            .join(User.user_info)
            .join(User.user_address)
            .join(User.processed_item)
            .join(User.payment_method)
            .join(User.payment_address)
            .join(User.subscription)
            .join(User.payment_history)
            .filter(User.deleted_at.is_(None)))
        
        users = result.all()

        for user in users:
            user.password = None

        data_response = {
            'msg':'Lista de usuários obtida com sucesso',
            'data':users
        }
        
        return data_response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f'Erro inesperado, tente novamente.\nDescrição: {e}')