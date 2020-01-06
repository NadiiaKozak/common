import json

from flask import request
from flask_restful import marshal_with, Resource

from db import db, Staff, Room
from models.parser import parser_staff, staff_room_parser
from models.structure import staff_structure, room_structure


class GetStaff(Resource):
    # get info about particular staff
    # get info about all staff
    @marshal_with(staff_structure)
    def get(self, staff_id=None):
        if staff_id:
            staff = Staff.query.get(staff_id)
            return staff if staff else "no such staff "
        else:
            return Staff.query.all()

    # add a new staff
    @marshal_with(staff_structure)
    def post(self):
        staff = json.loads(request.data)
        new_staff = Staff(**staff)
        db.session.add(new_staff)
        db.session.commit()
        return new_staff, 201

    # update info about staff
    @marshal_with(staff_structure)
    def patch(self):
        args_staff = parser_staff.parse_args()
        row = Staff.query.filter_by(staff_id=args_staff['staff_id']).first()
        if args_staff['staff_id']: row.staff_id = args_staff['staff_id']
        if args_staff['name']: row.name = args_staff['name']
        if args_staff['passport_id']: row.passport_id = args_staff['passport_id']
        if args_staff['position']: row.position = args_staff['position']
        if args_staff['salary']: row.salary = args_staff['salary']
        Staff.query.order_by(Staff.staff_id).all()
        db.session.commit()
        return row, 200

    # delete staff
    def delete(self):
        args = parser_staff.parse_args()
        delete_staff = Staff.query.get(args['staff_id'])
        if delete_staff:
            db.session.delete(delete_staff)
            db.session.commit()
            return "staff removed", 200
        else:
            return "you want to delete a non-existent staff, enter correctly"


class StaffRoom(Resource):
    def post(self):
        data = json.loads(request.data)
        number = data.get("number")
        staff_id = data.get("staff_id")
        room = Room.query.filter_by(number=number).first()
        staff = Staff.query.filter_by(staff_id=staff_id).first()
        staff.room_numbers.append(room)
        db.session.commit()
        return f"Successfully added {room.number} to {staff.name}"

    @marshal_with(room_structure)
    def get(self):
        args = staff_room_parser.parse_args(strict=True)
        staff = Staff.query.filter_by(name=args.get("name")).first()
        return staff.room_numbers
