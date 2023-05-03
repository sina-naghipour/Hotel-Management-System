from flask import Blueprint
from .room.routes import rooms
from .user.routes import users
api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(users)
api.register_blueprint(rooms)


