"""
Nome do arquivo: routes.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo responsável pelas rotas da aplicação Tax.
"""
from flask import Blueprint
from routes.auth.authRoute import bp as auth_bp
from routes.users.usersRoute import bp as users_bp

routes_bp = Blueprint('routes', __name__)
routes_bp.register_blueprint(auth_bp)
routes_bp.register_blueprint(users_bp)