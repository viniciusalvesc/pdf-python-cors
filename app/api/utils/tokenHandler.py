"""
Nome do arquivo: tokenJWT.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo de funcionalidades de tokens JWT.
"""
import time
from fastapi import HTTPException, status
from jose import jwt
from datetime import datetime, timedelta
from decouple import config

def generate_jwt(params):
    jwt_expires = config('JWT_EXPIRES')
    expiration_time = datetime.utcnow() + timedelta(days=int(jwt_expires[:-1]))
    params['exp'] = expiration_time
    return jwt.encode(params, config('JWT_SECRET'), algorithm=config('JWT_ALGORITHM'))

def decode_jwt(token: str):
    try:
        decoded_token = jwt.decode(token, config('JWT_SECRET'), algorithms=[config('JWT_ALGORITHM')])
        return decoded_token if decoded_token['exp'] >= time.time() else None
    except:
        return {}
