from datetime import datetime
from rest_api_demo.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(254), index=True, nullable=False)
    email = db.Column(db.String(254), index=True, unique=True, nullable=False)
    username = db.Column(db.String(254), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(254), nullable=False)
    
    id_user_type = db.Column(db.Integer, db.ForeignKey('user_type.id_user_type'))
    user_type = db.relationship('UserType', backref=db.backref('users', lazy='dynamic'))

    def __init__(self, name, email, username, password_hash, user_type):
        self.name = name
        self.email = email
        self.username = username
        self.password_hash = password_hash
        self.user_type = user_type
        print(user_type)

    def __repr__(self):
        return '<User %r>' % self.name

class UserType(db.Model):
    id_user_type = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(254), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User Type %r>' % self.name

class Business(db.Model):
    id_business = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(254))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    id_business_type = db.Column(db.Integer, db.ForeignKey('business_type.id_business_type'))

    def __repr__(self):
        return '<Business {}>'.format(self.name)

class BusinessType(db.Model):
    id_business_type = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(254))

    def __repr__(self):
        return '<Business Type {}>'.format(self.name)

class Establishment(db.Model):
    id_establishment = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(254))    
    id_business = db.Column(db.Integer, db.ForeignKey('business.id_business'))

    def __repr__(self):
        return '<Establishment {}>'.format(self.name)

class Location(db.Model):
    id_location = db.Column(db.Integer, primary_key=True, unique=True)
    address = db.Column(db.String(254))
    postal_code1 = db.Column(db.Integer)
    postal_code2 = db.Column(db.Integer)
    location = db.Column(db.String(254))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    id_establishment = db.Column(db.Integer, db.ForeignKey('establishment.id_establishment'))

    def __repr__(self):
        return '<Location{}>'.format(self.id_schedule_entry)

class Schedule(db.Model):
    id_schedule = db.Column(db.Integer, primary_key=True, unique=True)
    employee = db.Column(db.String(254))
    auto_accept = db.Column(db.Boolean, default=False)
    id_establishment = db.Column(db.Integer, db.ForeignKey('establishment.id_establishment'))

    def __repr__(self):
        return '<Schedule {}>'.format(self.id_schedule)

class ScheduleEntry(db.Model):
    id_schedule_entry = db.Column(db.Integer, primary_key=True, unique=True)
    start_date = db.Column(db.DateTime)
    id_schedule_status = db.Column(db.Integer, db.ForeignKey('schedule_status.id_schedule_status'))
    id_service = db.Column(db.Integer, db.ForeignKey('service.id_service'))
    id_schedule = db.Column(db.Integer, db.ForeignKey('schedule.id_schedule'))
    id_establishment = db.Column(db.Integer, db.ForeignKey('establishment.id_establishment'))

    def __repr__(self):
        return '<Schedule Entry {}>'.format(self.id_schedule_entry)

class ScheduleStatus(db.Model):
    id_schedule_status = db.Column(db.Integer, primary_key=True, unique=True)
    status = db.Column(db.String(254))

    def __repr__(self):
        return '<Schedule Status {}>'.format(self.status)

class Service(db.Model):
    id_service = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(254))
    duration = db.Column(db.Integer)
    price = db.Column(db.Float)
    id_establishment = db.Column(db.Integer, db.ForeignKey('establishment.id_establishment'))

    def __repr__(self):
        return '<Service {}>'.format(self.id_service)