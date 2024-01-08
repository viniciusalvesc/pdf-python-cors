"""
Nome do arquivo: initialize.py
Autor: Vinicius Alves Campello
Data de desenvolvimento: 07/01/2024
Descrição: Arquivo gerador da aplicação Flask com as respectivas configurações.
"""
from flask import Flask
from routes.routes import routes_bp
from decouple import config
from config.alchemy import db
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes_bp)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_DATABASE_URI')
    db.init_app(app)
    CORS(app)

    return app