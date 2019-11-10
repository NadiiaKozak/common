import json

from flask import Response
from flask_restful import Resource, reqparse

list_room = [{"Number": '001', "Level": 1, "Status": "free", "Price": 250.00},
             {"Number": '002', "Level": 2, "Status": "closed", "Price": 500.00},
             {"Number": "003", "Level": 3, "Status": "free", "Price": 500.00}]

parser = reqparse.RequestParser()
parser.add_argument('Number', location=['json'])
parser.add_argument('Level', type=int,  location=['json'])
parser.add_argument('Status',  location=['json'])
parser.add_argument('Price', type=float,  location=['json'])


class Rooms(Resource):
#get info about all rooms
    def get(self):
        return Response(json.dumps(list_room), status=200)


#get information about a particular room
#get information on all available rooms (use filter)
#get information about all closed rooms (use filter)
    def post(self):
        args = parser.parse_args()
        num_room = [i for i in list_room if i['Number'] == args['Number']]
        room_status = [i for i in list_room if i['Status'] == args['Status']]
        num_room.extend(room_status)
        return Response(json.dumps(num_room), status=200) if num_room else "no such room "

#update your number information
    def patch(self):
        args = parser.parse_args()
        for i in list_room:
            if i['Number'] == args['Number']:
                if args['Status'] is not None:
                    i['Status'] = args['Status']
                if args['Price'] is not None:
                    i['Price'] = args['Price']
        return Response(json.dumps(list_room), status=200)

#add a new room
    def put(self):
        args = parser.parse_args()
        list_room.append(args)
        return Response(json.dumps(list_room), status=200)

#delete number
    def delete(self):
        args = parser.parse_args()
        if args in list_room:
            list_room.remove(args)
        else:
            return "you want to delete a non-existent room, enter correctly"
        return Response(json.dumps(list_room), status=200)



