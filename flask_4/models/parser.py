from flask_restful import reqparse

parser_room = reqparse.RequestParser()
parser_room.add_argument('number', location=['json'])
parser_room.add_argument('level', type=int,  location=['json'])
parser_room.add_argument('status',  location=['json'])
parser_room.add_argument('price', type=float,  location=['json'])
parser_room.add_argument('tenant_id', type=int,  location=['json'])


parser_staff = reqparse.RequestParser()
parser_staff.add_argument('staff_id', location=['json'])
parser_staff.add_argument('name', required=True, help="Important: {error_msg}!!!", location=['json'])
parser_staff.add_argument('passport_id', type=int,  location=['json'])
parser_staff.add_argument('position',  location=['json'])
parser_staff.add_argument('salary', type=float,  location=['json'])


parser_tenant = reqparse.RequestParser()
parser_tenant.add_argument('id', location=['json'])
parser_tenant.add_argument('passport_id', location=['json'])
parser_tenant.add_argument('name', required=True, help="Important: {error_msg}!!!", location=['json'])
parser_tenant.add_argument('age', type=int, location=['json'])
parser_tenant.add_argument('sex', location=['json'])
parser_tenant.add_argument('city', location=['json'])
parser_tenant.add_argument('address', location=['json'])
parser_tenant.add_argument('number', location=['json'])


staff_room_parser = reqparse.RequestParser()
staff_room_parser.add_argument("name", required=True, help="Important: {error_msg}!!!")