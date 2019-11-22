from flask import request
from flask_restful import Resource, reqparse, marshal_with

from Tenants.structure_tenants import tenant_structure, list_tenants, Tenant

parser = reqparse.RequestParser()
parser.add_argument('passport_id', location=['json'])
parser.add_argument('name', location=['json'])
parser.add_argument('age', type=int, location=['json'])
parser.add_argument('address', location=['json'])
parser.add_argument('room_number', location=['json'])


class GetTenants(Resource):
    # get info about all tenants
    @marshal_with(tenant_structure)
    def get(self):
        return list_tenants

    # get info about particular tenant
    @marshal_with(tenant_structure)
    def post(self):
        result = [{'name': tenant.name, 'passport_id': tenant.passport_id, 'age': tenant.age, 'sex': tenant.sex,
                   'address': tenant.address, 'room_number': tenant.room_number} for tenant in list_tenants]
        args = parser.parse_args()
        particular_tenant = [i for i in result if i['passport_id'] == args['passport_id']]
        return particular_tenant if particular_tenant else "no such tenant "

    # update info about tenant
    @marshal_with(tenant_structure)
    def patch(self):
        tenant = parser.parse_args()
        chenge_tenant = request.get_json()
        for n, i in enumerate(list_tenants):
            if i.passport_id == tenant['passport_id']:
                list_tenants[n] = Tenant(**chenge_tenant)
        return "the changes were successful"

    # add a new tenant
    def put(self):
        new_tenant = request.get_json()
        list_tenants.append(Tenant(**new_tenant))
        return "add successfully"

    # delete staff
    def delete(self):
        delete_tenant = parser.parse_args()
        for n, i in enumerate(list_tenants):
            if i.passport_id == delete_tenant['passport_id']:
                list_tenants.remove(i)
                return "tenant removed"
        else:
            return "you want to delete a non-existent tenant, enter correctly"
