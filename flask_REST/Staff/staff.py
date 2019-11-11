from flask import request
from flask_restful import Resource, reqparse, marshal_with

from Staff.structure_staff import staff_structure, list_staff, Worker

parser = reqparse.RequestParser()
parser.add_argument('passport_id', location=['json'])
parser.add_argument('name', location=['json'])
parser.add_argument('position', location=['json'])
parser.add_argument('salary', location=['json'])


class GetStaff(Resource):
    # get info about all staff
    @marshal_with(staff_structure)
    def get(self):
        return list_staff

    #get info about particular staff
    @marshal_with(staff_structure)
    def post(self):
        result = [{'name': staff.name, 'passport_id': staff.passport_id, 'position': staff.position,
                   'salary': staff.salary} for staff in list_staff]
        args = parser.parse_args()
        particular_staff = [i for i in result if i['passport_id'] == args['passport_id']]
        return particular_staff if particular_staff else "no such staff "

    #update info about staff
    # @marshal_with(staff_structure)
    def patch(self):
        staff = parser.parse_args()
        chenge_staff = request.get_json()
        for n, i in enumerate(list_staff):
            if i.passport_id == staff['passport_id']:
                list_staff[n] = Worker(**chenge_staff)
                return "the changes were successful"
        else:
            return "you want to change a non-existent employee, enter correctly"


    #add a new worker
    def put(self):
        new_worker = request.get_json()
        list_staff.append(Worker(**new_worker))
        return "add successfully"

    #delete staff
    def delete(self):
        delete_staff = parser.parse_args()
        for n, i in enumerate(list_staff):
            if i.passport_id == delete_staff['passport_id']:
                list_staff.remove(i)
                return "employee removed"
        else:
            return "you want to delete a non-existent employee, enter correctly"
