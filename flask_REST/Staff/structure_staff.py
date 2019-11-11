from flask_restful import fields


class Worker:
    def __init__(self, name, passport_id, position, salary):
        self.name = name
        self.passport_id = passport_id
        self.position = position
        self.salary = salary

list_staff = [Worker("Vira", "RF123456", "manager", 1000),
             Worker("Nadiia", "KA654321", "cook", 750),
             Worker("Ljubov", "LM741852", "administrator", 500)]


staff_structure = {
    'name': fields.String,
    'passport_id': fields.String,
    'position': fields.String,
    'salary': fields.Float
}
