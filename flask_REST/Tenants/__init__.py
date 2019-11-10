from flask import Blueprint
from flask_restful import Api

from Tenants.tenants import GetTenants

api_tenants = Blueprint('tenants', __name__)
api = Api(api_tenants)

api.add_resource(GetTenants, "/tenants")