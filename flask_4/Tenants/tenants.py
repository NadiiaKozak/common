from flask import request
from flask_restful import marshal_with, Resource
import json

from db import db, Tenant
from models.parser import parser_tenant
from models.structure import tenant_structure, room_tenant


class GetTenants(Resource):
    # get info about all tenants
    # get info about particular tenant
    @marshal_with(tenant_structure)
    def get(self, tenant_id=None):
        if tenant_id:
            tenant = Tenant.query.get(tenant_id)
            return tenant if tenant else "no such tenant "
        else:
            return Tenant.query.all()

    # add a new tenant
    @marshal_with(tenant_structure)
    def post(self):
        new_tenant = json.loads(request.data)
        me = Tenant(**new_tenant)
        db.session.add(me)
        db.session.commit()
        return new_tenant, 201


    # update info about tenant
    @marshal_with(tenant_structure)
    def patch(self):
        args_tenant = parser_tenant.parse_args()
        row_tenant = Tenant.query.filter_by(passport_id=args_tenant['passport_id']).first()
        if args_tenant['name']: row_tenant.name = args_tenant['name']
        if args_tenant['passport_id']: row_tenant.passport_id = args_tenant['passport_id']
        if args_tenant['age']: row_tenant.age = args_tenant['age']
        if args_tenant['sex']: row_tenant.sex = args_tenant['sex']
        if args_tenant['city']: row_tenant.city = args_tenant['city']
        if args_tenant['address']: row_tenant.address = args_tenant['address']
        Tenant.query.order_by(Tenant.id).all()
        db.session.commit()
        return row_tenant, 200

    # delete tenant
    def delete(self):
        args = parser_tenant.parse_args()
        delete_tenant = Tenant.query.get(args['id'])
        if delete_tenant:
            db.session.delete(delete_tenant)
            db.session.commit()
            return "tenant removed",200
        else:
            return "you want to delete a non-existent tenant, enter correctly"


class TenantRoom(Resource):
    @marshal_with(room_tenant)
    def get(self, value):
        tenant = Tenant.query.get(value)
        return tenant.room_number
