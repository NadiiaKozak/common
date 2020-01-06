import json

from flask import request
from flask_restful import marshal_with, Resource

from db import db, Room
from models.parser import parser_room
from models.structure import room_structure


class Rooms(Resource):
    # get info about all rooms
    # get information about a particular room
    @marshal_with(room_structure)
    def get(self, number_room=None):
        if number_room:
            room = Room.query.get(number_room)
            return room if room else "no such room "
        else:
            return Room.query.all()

    # add a new room
    @marshal_with(room_structure)
    def post(self):
        room = json.loads(request.data)
        new_room = Room(**room)
        db.session.add(new_room)
        db.session.commit()
        return new_room, 201

    # update your number information
    @marshal_with(room_structure)
    def patch(self):
        args_room = parser_room.parse_args()
        row = Room.query.filter_by(number=args_room['number']).first()
        if args_room['number']: row.number = args_room['number']
        if args_room['level']: row.level = args_room['level']
        if args_room['status']: row.status = args_room['status']
        if args_room['price']: row.price = args_room['price']
        if args_room['tenant_id']: row.tenant_id = args_room['tenant_id']
        Room.query.order_by(Room.number).all()
        db.session.commit()
        return row, 200

    # get information on all available rooms (use filter)
    # get information about all closed rooms (use filter)
    @marshal_with(room_structure)
    def put(self):
        args_room = parser_room.parse_args()
        if args_room['status']: room_status = Room.query.filter_by(status=args_room['status']).all()
        return room_status if room_status else "no such room "

    # delete room
    def delete(self):
        args = parser_room.parse_args()
        delete_room = Room.query.get(args['number'])
        if delete_room:
            db.session.delete(delete_room)
            db.session.commit()
            return "room removed", 200
        else:
            return "you want to delete a non-existent room, enter correctly"

