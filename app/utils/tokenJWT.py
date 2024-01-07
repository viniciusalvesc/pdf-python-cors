import os
from flask import Flask, request, jsonify
from werkzeug.exceptions import Unauthorized
import jwt
from datetime import datetime, timedelta


def generate_jwt(params):
    jwt_expires = os.getenv('JWT_EXPIRES')
    expiration_time = datetime.utcnow() + timedelta(days=int(jwt_expires[:-1]))
    params['exp'] = expiration_time
    # return jwt.encode(params, os.getenv('JWT_SECRET'), algorithm='HS256').decode('utf-8')
    return jwt.encode(params, os.getenv('JWT_SECRET'), algorithm='HS256')

def verify_jwt(token):
    try:
        decoded_token = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])

        if not decoded_token:
            raise Unauthorized('Token Inválido')

        return jsonify({'message': 'Token Válido'})
    except jwt.ExpiredSignatureError:
        raise Unauthorized('Token Expirado')
    except jwt.InvalidTokenError:
        raise Unauthorized('Token Inválido')