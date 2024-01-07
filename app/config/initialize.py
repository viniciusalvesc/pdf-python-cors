from flask import Flask
from routes.routes import routes_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes_bp)
    return app