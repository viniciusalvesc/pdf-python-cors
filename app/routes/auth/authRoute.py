"""
Nome do arquivo: authRoute.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo responsável pela rota de login do usuário.
"""
from services.pusherService import PusherService
from flask import Blueprint, jsonify, request
from models.users.Users import Users
from utils.tokenJWT import generate_jwt
import flask_bcrypt

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    try:
        body = request.json
        email = body.get('email')
        password = body.get('password')
        _session = body.get('_session')

        if not email or not password:
            return jsonify('Por favor informe o email e senha.'), 400

        user = Users.query.filter_by(email=email).first()

        if not user:
            return jsonify('Email não cadastrado'), 404

        if not flask_bcrypt.check_password_hash(user.password, password):
            return jsonify('Email ou senha inválidos'), 401

        user.password = None

        data_response = {
            'msg':'Usuário autenticado com sucesso',
            'data':{
                'token': generate_jwt({'id': user.id, 'email': user.email, 'role': user.role}),
                'user': user.serialize()
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

        return jsonify(data_response), 200
    except Exception as e:
        print(e)
        return jsonify({'error': f'Ocorreu um erro ao realizar login.\nDescrição: {e}'}), 500