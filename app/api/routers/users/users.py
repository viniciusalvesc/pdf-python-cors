"""
Nome do arquivo: authRoute.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 15/01/2024
Descrição: Arquivo responsável pela rota de usuários.
"""
from fastapi import APIRouter, Depends, HTTPException
from app.api.models.ft_user import UserRepository 
from sqlalchemy.orm import Session
from app.api.utils.tokenAuth import TokenAuth
from app.db.sqlalchemy import get_db
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
users_router = APIRouter(prefix="/users")

@users_router.get('/{email}')
async def find_one(email: str, db: Session = Depends(get_db)):
    try:
        user = await UserRepository.get_user_info_address(email, db)

        if not user:
            raise HTTPException(status_code=404, detail='Usuário não encontrado')
        
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


@users_router.get('/', dependencies=[Depends(TokenAuth())])
async def find_all(db: Session = Depends(get_db)):
    try:
        users = await UserRepository.get_all_active_users(db)

        data_response = {
            'msg':'Lista de usuários obtida com sucesso',
            'data':users
        }
        
        return data_response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f'Erro inesperado, tente novamente.\nDescrição: {e}')
    
@users_router.get('/settings/', dependencies=[Depends(TokenAuth())])
async def find_one_settings(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        user = await UserRepository.get_user_by_token(token, db)

        if not user:
            raise HTTPException(status_code=404, detail='Usuário não encontrado')

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
