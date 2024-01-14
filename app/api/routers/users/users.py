# """
# Nome do arquivo: authRoute.py
# Autor: Vinicius Alves Campello
# Data de desenvolvimento: 09/01/2024
# Descrição: Arquivo responsável pela rota de usuários.
# """
# from fastapi import APIRouter
# from api.models.ft_user_address.UserAddress import UserAddress
# from api.models.ft_user.User import User
# from api.models.ft_user_info.UserInfo import UserInfo
# from config.alchemy import db

# bp = Blueprint('users', __name__, url_prefix='/users')

# @bp.route('/<email>', methods=['GET'])
# def findOne(email):
#     try:
#         user = (
#             db.session.query(User)
#             .join(UserInfo, User.id == UserInfo.user_id)
#             .join(UserAddress, User.id == UserAddress.user_id)
#             .filter(User.email == email)
#             .first()
#         )
        
#         user.password = None

#         data_response = {
#             'msg':'Usuário encontrado',
#             'data':{
#                 'user': user.serialize()
#             }
#         }
        
#         return jsonify(data_response), 200
#     except Exception as e:
#         print(e)
#         return jsonify({'error': f'Erro inesperado, tente novamente.\nDescrição: {e}'}), 500
