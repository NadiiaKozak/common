from flask import request
from flask_restful import Resource, reqparse, marshal_with

from Rooms.structure_rooms import room_structure, list_room, Room

parser = reqparse.RequestParser()
parser.add_argument('room_number', location=['json'])
parser.add_argument('level', type=int,  location=['json'])
parser.add_argument('status',  location=['json'])
parser.add_argument('price', type=float,  location=['json'])


class Rooms(Resource):
    #get info about all rooms
    @marshal_with(room_structure)
    def get(self):
        return list_room

    # get information about a particular room
    # get information on all available rooms (use filter)
    # get information about all closed rooms (use filter)
    @marshal_with(room_structure)
    def post(self):
        args = parser.parse_args()
        result = [{'room_number': room.room_number, 'level': room.level, 'status': room.status,
                   'price': room.price} for room in list_room]
        num_room = [i for i in result if i['room_number'] == args['room_number']]
        room_status = [i for i in result if i['status'] == args['status']]
        num_room.extend(room_status)
        return num_room if num_room else "no such room "


    #update your number information
    @marshal_with(room_structure)
    def patch(self):
        args = parser.parse_args()
        chenge_room = request.get_json()
        for n, i in enumerate(list_room):
            if i.room_number == args['room_number']:
                list_room[n] = Room(**chenge_room)
        return "the changes were successful"

    # add a new room
    def put(self):
        new_room = request.get_json()
        list_room.append(Room(**new_room))
        return "add successfully"


    #delete number
    def delete(self):
        delete_room = parser.parse_args()
        for n, i in enumerate(list_room):
            if i.room_number == delete_room['room_number']:
                list_room.remove(i)
                return "room removed"
        else:
            return "you want to delete a non-existent room, enter correctly"




