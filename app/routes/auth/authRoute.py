from services.pusherService import PusherService
from flask import Blueprint, jsonify, request
from models.user.Users import Users
from utils.tokenJWT import generate_jwt
import flask_bcrypt

# rota com prefixo auth
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    try:
        # return jsonify({
        #         "access_token": email,
        #         "user": password
        #     }), 200

        body = request.json
        email = body.get('email')
        password = body.get('password')
        _session = body.get('_session')

        if not email or not password:
            return jsonify('Por favor informe o email e senha.'), 400

        user = Users.query.filter_by(email=email).first()

        if not user:
            return jsonify('Email não cadastrado'), 404

        # compara hash
        if not flask_bcrypt.check_password_hash(user.password, password):
            return jsonify('Email ou senha inválidos'), 401

        # ocultando a senha do banco
        user.password = None

        data_response = {
            'token': generate_jwt({'id': user.id, 'email': user.email, 'role': user.role}),
            'user': user.serialize()
        }

        data_session = {
            'status': 'connected',
            'message': 'Nova sessão iniciada!',
            'session': {
                'id': _session,
            },
        }

        # utilizando o Pusher para o disparo de eventos
        PusherService().send_trigger(
            f'session_user_{user.id}',
            'created_session',
            data_session
        )

        return jsonify('Usuário autenticado com sucesso', data_response), 200
    except Exception as e:
        print(e)
        return jsonify({'error': f'Ocorreu um erro ao realizar login.\nDescrição: {e}'}), 500