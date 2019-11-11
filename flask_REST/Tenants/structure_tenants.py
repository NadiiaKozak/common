from flask_restful import fields


class Tenant:
    def __init__(self, name, passport_id, age, sex, address, room_number):
        self.name = name
        self.passport_id = passport_id
        self.age = age
        self.sex = sex
        self.address = address
        self.room_number = room_number

list_tenants = [Tenant("Oleg", "UA123456", 21, "M", {
                                                        "city": "Kyiv",
                                                        "street": " Svobody"}, "003"),
               Tenant("Mariia", "UK456789", 34, "F", {
                                                       "city": "Odesa",
                                                       "street": " Shevchenka"}, "002"),
               Tenant("Yurij", "UB741963", 44, "M", {
                                                       "city": "Lviv",
                                                       "street": " Mazepy"}, "001")]


address_structure = {
    'city': fields.String,
    'street': fields.String
}

tenant_structure = {
    'name': fields.String,
    'passport_id': fields.String,
    'age': fields.Integer,
    'sex': fields.String,
    'address': fields.Nested(address_structure),
    'room_number': fields.String
}
