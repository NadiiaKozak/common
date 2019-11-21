from flask import request
from flask_restful import marshal_with, Resource
import json

from db import db, Tenant
from models.parser import parser_tenant
from models.structure import tenant_structure, room_tenant


class GetTenants(Resource):
    # get info about all tenants
    @marshal_with(tenant_structure)
    def get(self):
        return Tenant.query.all()

    # get info about particular tenant
    @marshal_with(tenant_structure)
    def post(self):
        args = parser_tenant.parse_args()
        particular_tenant = Tenant.query.get(args['id'])
        return particular_tenant if particular_tenant else "no such tenant "


    # update info about tenant
    @marshal_with(tenant_structure)
    def patch(self):
        args_tenant = parser_tenant.parse_args()
        row_tenant = Tenant.query.filter_by(passport_id=args_tenant['passport_id']).first()
        if args_tenant['name'] is not None: row_tenant.name = args_tenant['name']
        if args_tenant['passport_id'] is not None: row_tenant.passport_id = args_tenant['passport_id']
        if args_tenant['age'] is not None: row_tenant.age = args_tenant['age']
        if args_tenant['sex'] is not None: row_tenant.sex = args_tenant['sex']
        if args_tenant['city'] is not None: row_tenant.city = args_tenant['city']
        if args_tenant['address'] is not None: row_tenant.address = args_tenant['address']
        Tenant.query.order_by(Tenant.id).all()
        db.session.commit()
        return "the changes were successful"

    # add a new tenant
    def put(self):
        new_tenant = json.loads(request.data)
        me = Tenant(**new_tenant)
        db.session.add(me)
        db.session.commit()
        return "add successfully"
    

    # delete staff
    def delete(self):
        delete_tenant = Tenant.query.get(parser_tenant.parse_args().get('id'))
        db.session.delete(delete_tenant)
        db.session.commit()
        return "tenant removed"

class TenantRoom(Resource):
    @marshal_with(room_tenant)
    def get(self, value):
        tenant = Tenant.query.get(value)
        return tenant.room_number
