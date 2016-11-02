"""
Models page for website with each pillar and its attributes
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sweetOutdoors:wearefine@sweetoutdoorsdb.ckneyrny5ckj.us-west-2.rds.amazonaws.com:5432/sweetOutdoors'
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
    zipcode = db.Column(db.Integer)

    state_id_fk = db.Column(db.Integer, db.ForeignKey('States.idnum'), nullable=True)

    events = db.relationship('Event', backref='Park', lazy='dynamic')
    campgrounds_rel = db.relationship(
        'Campground', backref='Park', lazy='dynamic')

    def __init__(self, name, latitude, longitude, address, phone, rating, website,
                 zipcode):

        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.address = address
        self.phone = phone
        self.rating = rating
        self.website = website
        self.zipcode = zipcode

    def __repr__(self):
        return '<Park %r>' % self.name


class Event(db.Model):

    """Event class with initializer to document models"""
    __tablename__ = 'Events'

    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    latitude = db.Column(db.String(256))
    longitude = db.Column(db.String(256))
    category = db.Column(db.String(256))
    startDate = db.Column(db.String(256))
    endDate = db.Column(db.String(256))
    urlAdr = db.Column(db.String(256))
    organizationName = db.Column(db.String(256))
    homePageUrlAdr = db.Column(db.String(256)) #organization URL
    cityName = db.Column(db.String(256))
    zipcode = db.Column(db.Integer)

    park_id_fk = db.Column(db.Integer, db.ForeignKey('Parks.idnum'), nullable=True)
    state_id_fk = db.Column(db.Integer, db.ForeignKey('States.idnum'), nullable=True)

    def __init__(self, name, latitude, longitude, category, startDate, endDate, urlAdr, organizationName, 
                 homePageUrlAdr, cityName, zipcode):

        self.name = name
        selv.latitude = latitude
        self.longitude = longitude
        self.category = category
        self.startDate = startDate
        self.endDate = endDate
        self.urlAdr = urlAdr
        self.organizationName = organizationName
        self.zipcode = zipcode
        self.cityName = cityName

    def __repr__(self):
        return '<Event %r>' % self.name


class State(db.Model):

    """State class with initializer to document models"""
    __tablename__ = 'States'

    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    description = db.Column(db.String(2048))
    total_area = db.Column(db.Float)
    population = db.Column(db.Integer)
    highestPoint = db.Column(db.String(256))

    campgrounds_rel = db.relationship(
        'Campground', backref='State', lazy='dynamic')
    parks_rel = db.relationship('Park', backref='State', lazy='dynamic')
    events_rel = db.relationship(
        'Event', backref='State', lazy='dynamic')

    def __init__(self, name, description, total_area, population, highestPoint):
        self.name = name
        self.description = description
        self.total_area = total_area
        self.population = population
        self.highestPoint = highestPoint

    def __repr__(self):
        return '<State %r>' % self.name


class Campground(db.Model):

    """Campground class with initializer to document models"""
    __tablename__ = 'Campgrounds'

    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    description = db.Column(db.String(2048))
    cost = db.Column(db.String(256))
    latitude = db.Column(db.String(256))
    longitude = db.Column(db.String(256))
    accessibilty = db.Column(db.Boolean)
    reservation_url = db.Column(db.String(256))
    email = db.Column(db.String(256))
    zipcode = db.Column(db.Integer)
    state = db.Column(db.String(256))

    park_id_fk = db.Column(db.Integer, db.ForeignKey('Parks.idnum'), nullable=True)
    state_id_fk = db.Column(db.Integer, db.ForeignKey('States.idnum'), nullable=True)

    def __init__(self, name, description, cost, latitude, longitude, accessibility,
                 reservation_url, email, zipcode, state):
        self.name = name
        self.description = description
        self.cost = cost
        self.longitude = longitude
        self.latitude = latitude
        self.accessibility = accessibility
        self.reservation_url = reservation_url
        self.email = email
        self.zipcode = zipcode
        self.state = state

    def __repr__(self):
        return '<Campgrounds %r>' % self.name