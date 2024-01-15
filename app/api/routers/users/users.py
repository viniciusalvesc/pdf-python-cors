"""
Nome do arquivo: authRoute.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 15/01/2024
Descrição: Arquivo responsável pela rota de usuários.
"""
from fastapi import APIRouter, Depends, HTTPException
from app.api.models.ft_user.User import User
from app.api.models.ft_user_address.UserAddress import UserAddress
from app.api.models.ft_user_info.UserInfo import UserInfo
from sqlalchemy.orm import Session
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
