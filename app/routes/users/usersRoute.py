"""
Nome do arquivo: authRoute.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo responsável pela rota de usuários.
"""
from utils.logger import logger
from services.pusherService import PusherService
from flask import Blueprint, jsonify, request
from models.users.Users import Users
from sqlalchemy.orm import joinedload
from config.alchemy import db

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/<email>', methods=['GET'])
def findOne(email):
    try:
        user_with_personal_info = (
            db.session.query(Users)
            .filter_by(email=email)
            .join(Users.personal_info)
            .options(joinedload(Users.personal_info))
            .first()
        )
        if user_with_personal_info:
            return jsonify(user_with_personal_info)
       
        return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        logger.error(f'[__main__]: {e}')