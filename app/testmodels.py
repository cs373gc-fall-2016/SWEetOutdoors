"""
Models page for website with each pillar and its attributes
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

#pylint:disable=invalid-name, too-many-arguments, too-few-public-methods, too-many-instance-attributes

class Park(db.Model):

    """Park class with initializer to document models"""
    __tablename__ = 'Parks'

    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    latitude = db.Column(db.String(256))
    longitude = db.Column(db.String(256))
    address = db.Column(db.String(256))
    phone = db.Column(db.String(256))
    rating = db.Column(db.Float)
    website = db.Column(db.String(256))
    zipcode = db.Column(db.String(256))
    zipregion = db.Column(db.String(256))
    photo_url = db.Column(db.String(1024))

    state_fk = db.Column(db.String(256), db.ForeignKey('States.name'), nullable=True)

    events = db.relationship('Event', backref='Park', lazy='dynamic')
    campgrounds_rel = db.relationship(
        'Campground', backref='Park', lazy='dynamic')

    def __init__(self, name, latitude, longitude, address, phone, rating, website,
                 zipcode, photo, zipregion, state):

        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.address = address
        self.phone = phone
        self.rating = rating
        self.website = website
        self.zipcode = zipcode
        self.photo_url = photo
        self.zipregion = zipregion
        self.state_fk = state

    def __repr__(self):
        return '<Park %r>' % self.name


class Event(db.Model):

    """Event class with initializer to document models"""
    __tablename__ = 'Events'

    idnum = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.String(256))
    longitude = db.Column(db.String(256))
    topics = db.Column(db.String(256))

    start_date = db.Column(db.String(256))
    end_date = db.Column(db.String(256))
    pic_url = db.Column(db.String(2048))
    
    org_name = db.Column(db.String(512))
    
    contact_phone_num = db.Column(db.String(256))
    city = db.Column(db.String(256))
    zipcode = db.Column(db.String(256))
    zipregion = db.Column(db.String(256))
    # state = string

    park_fk = db.Column(db.Integer, db.ForeignKey('Parks.idnum'), nullable=True)
    state_fk = db.Column(db.String(256), db.ForeignKey('States.name'), nullable=True)

    def __init__(self, latitude, longitude, topics, start_date, end_date, pic_url, org_name, 
                 contact_phone_num, zipcode, city, zipregion, state_fk):

        self.latitude = latitude
        self.longitude = longitude
        self.topics = topics
        self.start_date = start_date
        self.end_date = end_date
        self.pic_url = pic_url
        self.org_name = org_name + "'s Event"
        self.contact_phone_num = contact_phone_num
        if contact_phone_num == "":
            self.contact_phone_num = "(555) 555-5555"
        self.city = city
        self.zipcode = zipcode
        self.zipregion = zipregion
        self.state_fk = state_fk

    def __repr__(self):
        return '<Event %r>' % self.org_name


class State(db.Model):

    """State class with initializer to document models"""
    __tablename__ = 'States'

    name = db.Column(db.String(256), primary_key = True)
    description = db.Column(db.String(2048))
    total_area = db.Column(db.String(256))
    population = db.Column(db.String(256))
    highest_point = db.Column(db.String(256))
   

    campgrounds_rel = db.relationship(
        'Campground', backref='State', lazy='dynamic')
    parks_rel = db.relationship('Park', backref='State', lazy='dynamic')
    events_rel = db.relationship(
        'Event', backref='State', lazy='dynamic')

    def __init__(self, name, description, total_area, population, highest_point):
        self.name = name
        self.description = description
        self.total_area = total_area
        self.population = population
        self.highest_point = highest_point

    def __repr__(self):
        return '<State %r>' % self.name


class Campground(db.Model):

    """Campground class with initializer to document models"""
    __tablename__ = 'Campgrounds'

    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    description = db.Column(db.String(4096))
    latitude = db.Column(db.String(256))
    longitude = db.Column(db.String(256))
    direction = db.Column(db.String(4096))
    phone = db.Column(db.String(256))
    email = db.Column(db.String(256))
    zipcode = db.Column(db.Integer)

    park_fk = db.Column(db.Integer, db.ForeignKey('Parks.idnum'), nullable=True)
    state_fk = db.Column(db.String(256), db.ForeignKey('States.name'), nullable=True)

    def __init__(self, name, description, latitude, longitude, direction, phone, email, zipcode, state):
        self.name = name
        self.description = description
        if description == "":
            self.description == "No Description Available."
        self.longitude = longitude
        self.latitude = latitude
        self.direction = direction
        if direction == "":
            self.direction = "No Directions Available. Go Google It."
        self.phone = phone
        if phone == "":
            self.phone == "(555) 555-5555"
        self.email = email
        if email == "":
            self.email == "No Email Available. "
        self.zipcode = zipcode
        self.state_fk = state

    def __repr__(self):
        return '<Campgrounds %r>' % self.name
