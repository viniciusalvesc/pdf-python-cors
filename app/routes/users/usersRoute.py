"""
Nome do arquivo: authRoute.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 09/01/2024
Descrição: Arquivo responsável pela rota de usuários.
"""
from models.user_address.UserAddress import UserAddress
from flask import Blueprint, jsonify
from models.users.Users import Users
from models.user_info.UserInfo import UserInfo
from config.alchemy import db

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/<email>', methods=['GET'])
def findOne(email):
    try:
        user = (
            db.session.query(Users)
            .join(UserInfo, Users.id == UserInfo.user_id)
            .join(UserAddress, Users.id == UserAddress.user_id)
            .filter(Users.email == email)
            .first()
        )
        
        user.password = None

        data_response = {
            'msg':'Usuário encontrado',
            'data':{
                'user': user.serialize()
            }
        }
        
        return jsonify(data_response), 200
    except Exception as e:
        print(e)
        return jsonify({'error': f'Erro inesperado, tente novamente.\nDescrição: {e}'}), 500
