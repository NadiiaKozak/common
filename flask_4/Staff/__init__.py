from flask import Blueprint
from flask_restful import Api

from Staff.staff import GetStaff, StaffRoom

api_staff = Blueprint('staff', __name__)
api = Api(api_staff)

api.add_resource(GetStaff, "/staff", "/staff/<staff_id>")
api.add_resource(StaffRoom, "/staff_room")
