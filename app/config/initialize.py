from flask import Flask
from routes.routes import routes_bp
from decouple import config
from config.alchemy import db
import os
from flask_bcrypt import Bcrypt

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes_bp)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    db.init_app(app)

    return app