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
from models.personalInfo.PersonalInfo import PersonalInfo
from config.alchemy import db

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/<email>', methods=['GET'])
def findOne(email):
    # try:
    #     user_with_personal_info = (
    #         db.session.query(Users)
    #         .filter_by(email=email)
    #         .join(Users.personal_info)
    #         .options(joinedload(Users.personal_info))
    #         .first()
    #     )
    #     if user_with_personal_info:
    #         return jsonify(user_with_personal_info)
       
    #     return jsonify({'error': 'User not found'}), 404
    # except Exception as e:
    #     logger.error(f'[__main__]: {e}')
    
        # .join(Users.personal_info)

    # user_with_personal_info = (
    #     db.session.query(PersonalInfo)
    #     .filter(PersonalInfo.userId == email)
    #     .first()
    # )

    print(email)

    user = (
        db.session.query(Users)
        .join(PersonalInfo, Users.id == PersonalInfo.userId)
        .filter(Users.email == email)
        .first()
    )
    
    user.password = None

    # print(dir(PersonalInfo))

    print((user.serialize()))

    # result = user.first()

    if user:

        return jsonify(user.serialize()), 200
    
    return jsonify({'msg': 'query retornou nada'}), 404
