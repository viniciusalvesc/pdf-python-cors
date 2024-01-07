from flask import Blueprint
from routes.auth.authRoute import bp as auth_bp

routes_bp = Blueprint('routes', __name__)
routes_bp.register_blueprint(auth_bp)