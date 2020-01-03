from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


room_staff = db.Table(
    'room_staff',
    db.Column('staff_id', db.Integer, db.ForeignKey('staff.staff_id')),
    db.Column('number', db.Integer, db.ForeignKey('room.number'))
)


class Tenant(db.Model):
    __tablename__ = 'tenant'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    passport_id = db.Column(db.String)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(7))
    city = db.Column(db.String)
    address = db.Column(db.String)
    # room_number = db.Column(db.Integer, db.ForeignKey('room.number'))
    room_number = db.relationship('Room', backref='tenant')


class Room(db.Model):
    __tablename__ = 'room'
    number = db.Column(db.Integer, autoincrement=True, primary_key=True)
    level = db.Column(db.Integer)
    status = db.Column(db.String(10))
    price = db.Column(db.Float)
    # tenant_id = db.relationship('Tenant', backref='room')
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'))


class Staff(db.Model):
    __tablename__ = 'staff'
    staff_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    passport_id = db.Column(db.String)
    position = db.Column(db.String)
    salary = db.Column(db.Float)
    room_numbers = db.relationship('Room', secondary=room_staff, backref=db.backref('staff'))

