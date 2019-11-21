import json

from flask import request
from flask_restful import marshal_with, Resource

from db import db, Room
from models.parser import parser_room
from models.structure import room_structure


class Rooms(Resource):
    # get info about all rooms
    @marshal_with(room_structure)
    def get(self):
        return Room.query.all()

    # get information about a particular room
    # get information on all available rooms (use filter)
    # get information about all closed rooms (use filter)
    @marshal_with(room_structure)
    def post(self):
        args_room = parser_room.parse_args()
        if args_room['number'] is not None: particular_room = Room.query.get(args_room['number'])
        if args_room['status'] is not None: particular_room = Room.query.filter_by(status=args_room['status']).all()
        return particular_room if particular_room else "no such room "

    # update your number information
    @marshal_with(room_structure)
    def patch(self):
        args_room = parser_room.parse_args()
        row = Room.query.filter_by(number=args_room['number']).first()
        if args_room['number'] is not None: row.number = args_room['number']
        if args_room['level'] is not None: row.level = args_room['level']
        if args_room['status'] is not None: row.status = args_room['status']
        if args_room['price'] is not None: row.price = args_room['price']
        if args_room['tenant_id'] is not None: row.tenant_id = args_room['tenant_id']
        Room.query.order_by(Room.number).all()
        db.session.commit()
        return "the changes were successful"

    # add a new room
    def put(self):
        room = json.loads(request.data)
        new_room = Room(**room)
        db.session.add(new_room)
        db.session.commit()
        return "add successfully"

    # delete room
    def delete(self):
        delete_room = Room.query.get(parser_room.parse_args().get('number'))
        db.session.delete(delete_room)
        db.session.commit()
        return "room removed"
