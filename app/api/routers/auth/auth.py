"""
Nome do arquivo: authRoute.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo responsável pela rota de login do usuário.
"""
from fastapi import APIRouter, Depends, HTTPException
from app.api.models.ft_user.User import User
import app.api.models.ft_user_address.UserAddress
import app.api.models.ft_user_info.UserInfo
from app.api.schemas.auth_route import LoginRequest
from app.api.services.pusherService import PusherService
from sqlalchemy.orm import Session
from app.api.utils.tokenHandler import generate_jwt
from app.db.sqlalchemy import get_db
import bcrypt

auth_router = APIRouter(prefix="/auth")

@auth_router.post('/login')
async def login(request_data: LoginRequest, db: Session = Depends(get_db)):
    try:
        email = request_data.email
        password = request_data.password
        _session = request_data.session

        if not email or not password:
            raise HTTPException(status_code=400, detail='Por favor, informe o email e senha.')

        user = db.query(User).filter(User.email == email).first()


        if not user or not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            raise HTTPException(status_code=401, detail='Email ou senha inválidos')

        user.password = None

        data_response = {
            'msg': 'Usuário autenticado com sucesso',
            'data': {
                'token': generate_jwt({'id': user.id, 'email': user.email, 'role': user.role}),
                'user': user
            }
        }

        data_session = {
            'status': 'connected',
            'message': 'Nova sessão iniciada!',
            'session': {
                'id': _session,
            },
        }

        PusherService().send_trigger(
            f'session_user_{user.id}',
            'created_session',
            data_session
        )

        return data_response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f'Ocorreu um erro ao realizar login.\nDescrição: {e}')