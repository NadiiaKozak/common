from flask_restful import fields


class Room:
    def __init__(self, room_number, level, status, price):
        self.room_number = room_number
        self.level = level
        self.status = status
        self.price = price


list_room = [Room("001", 1, "free", 250.00),
             Room('002', 2, "closed", 500.00),
             Room("003", 3, "free", 500.00)]


room_structure = {
    'room_number': fields.String,
    'level': fields.Integer,
    'status': fields.String,
    'price': fields.Float
}
