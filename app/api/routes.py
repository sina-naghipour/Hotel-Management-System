from flask import Blueprint
from .room.routes import rooms
from .user.routes import users
from .menu.routes import menu
api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(users)
api.register_blueprint(rooms)
api.register_blueprint(menu)


