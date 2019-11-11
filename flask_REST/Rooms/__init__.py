from flask import Blueprint
from flask_restful import Api

from Rooms.rooms import Rooms

api_rooms = Blueprint('rooms', __name__)
api = Api(api_rooms)

api.add_resource(Rooms, "/rooms")
