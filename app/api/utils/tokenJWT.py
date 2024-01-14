"""
Nome do arquivo: tokenJWT.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo de funcionalidades de tokens JWT.
"""
from flask import jsonify
from werkzeug.exceptions import Unauthorized
import jwt
from datetime import datetime, timedelta
from decouple import config


def generate_jwt(params):
    jwt_expires = config('JWT_EXPIRES')
    expiration_time = datetime.utcnow() + timedelta(days=int(jwt_expires[:-1]))
    params['exp'] = expiration_time
    return jwt.encode(params, config('JWT_SECRET'), algorithm='HS256')

def verify_jwt(token):
    try:
        decoded_token = jwt.decode(token, config('JWT_SECRET'), algorithms=['HS256'])

        if not decoded_token:
            raise Unauthorized('Token Inválido')

        return jsonify({'message': 'Token Válido'})
    except jwt.ExpiredSignatureError:
        raise Unauthorized('Token Expirado')
    except jwt.InvalidTokenError:
        raise Unauthorized('Token Inválido')