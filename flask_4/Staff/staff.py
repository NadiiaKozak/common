import json

from flask import request
from flask_restful import marshal_with, Resource

from db import db, Staff, Room
from models.parser import parser_staff, staff_room_parser
from models.structure import staff_structure, room_structure


class GetStaff(Resource):
    # get info about all staff
    @marshal_with(staff_structure)
    def get(self):
        return Staff.query.all()

    # get info about particular tenant
    @marshal_with(staff_structure)
    def post(self):
        args = parser_staff.parse_args()
        particular_staff = Staff.query.get(args['staff_id'])
        return particular_staff if particular_staff else "no such tenant "

    # update info about staff
    @marshal_with(staff_structure)
    def patch(self):
        args_staff = parser_staff.parse_args()
        row = Staff.query.filter_by(staff_id=args_staff['staff_id']).first()
        if args_staff['staff_id'] is not None: row.staff_id = args_staff['staff_id']
        if args_staff['name'] is not None: row.name = args_staff['name']
        if args_staff['passport_id'] is not None: row.passport_id = args_staff['passport_id']
        if args_staff['position'] is not None: row.position = args_staff['position']
        if args_staff['salary'] is not None: row.salary = args_staff['salary']
        Staff.query.order_by(Staff.staff_id).all()
        db.session.commit()
        return "the changes were successful"

    # add a new staff
    def put(self):
        staff = json.loads(request.data)
        new_staff = Staff(**staff)
        db.session.add(new_staff)
        db.session.commit()
        return "add successfully"
    
    #delete staff
    def delete(self):
        delete_staff = Staff.query.get(parser_staff.parse_args().get('staff_id'))
        db.session.delete(delete_staff)
        db.session.commit()
        return "staff removed"



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
