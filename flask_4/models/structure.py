from flask_restful import fields

tenant_room = {'id': fields.Integer,
               'name': fields.String}


room_tenant = {
    'number': fields.Integer,
    'level': fields.Integer,
    'price': fields.Float
}

room_structure = {
    'number': fields.Integer,
    'level': fields.Integer,
    'status': fields.String,
    'price': fields.Float,
    'tenant_id': fields.Integer
}


staff_structure = {
    'staff_id': fields.Integer,
    'name': fields.String,
    'passport_id': fields.String,
    'position': fields.String,
    'salary': fields.Float
}


tenant_structure = {
    'id': fields.Integer,
    'name': fields.String,
    'passport_id': fields.String,
    'age': fields.Integer,
    'sex': fields.String,
    'city': fields.String,
    'address': fields.String,
    'room_number': fields.Nested(room_tenant)
}

