from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
 
class Parks(db.Model):
    __tablename__ = 'Parks'

    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    price = db.Column(db.Float)
    opentime = db.Column(db.Integer)
    closetime = db.Column(db.Integer)
    website = db.Column(db.String(256))
    zipcode = db.Column(db.Integer)

    state_id_fk = db.Column(db.Integer, db.ForeignKey('States.idnum')) 

    events = db.relationship('Events', backref = 'Parks', lazy = 'dynamic')
    campgrounds_rel = db.relationship('Campgrounds', backref = 'Parks', lazy = 'dynamic')
 
    def __init__(self, name, price, opentime, closetime, website, zipcode, state_id_fk):

        self.name = name
        self.price = price
        self.opentime = opentime
        self.closetime = closetime
        self.website = website
        self.zipcode = zipcode
        self.state_id_fk = state_id_fk
 
    def __repr__(self):
            return '<Park %r>' % self.name
 
class Events(db.Model):
    __tablename__ = 'Events'
 
    idnum = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256))
    category = db.Column(db.String(256))
    startDate = db.Column(db.String(256))# may need to change
    email = db.Column(db.String(256))
    url = db.Column(db.String(256))
    zipcode = db.Column(db.Integer)

    park_id_fk = db.Column(db.Integer, db.ForeignKey('Parks.idnum'))
    state_id_fk = db.Column(db.Integer, db.ForeignKey('States.idnum')) 
 
    def __init__(self, name, category, startDate, email, url, zipcode, park_id_fk, state_id_fk):

        self.name = name
        self.category = category
        self.startDate = startDate
        self.email = email
        self.url = url
        self.zipcode = zipcode
        self.park_id_fk = park_id_fk
        self.state_id_fk = state_id_fk
 
    def __repr__(self):
            return '<Event %r>' % self.name
 

class States(db.Model):
    __tablename__ = 'States'

    idnum = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256))
    highestPoint = db.Column(db.String(256))
    population = db.Column(db.Integer)
    description = db.Column(db.String(2048))
    total_area = db.Column(db.Float)

    campgrounds_rel = db.relationship('Campgrounds', backref = 'States', lazy = 'dynamic')
    parks_rel = db.relationship('Parks', backref = 'States', lazy = 'dynamic')
    events_rel = db.relationship('Events', backref = 'States', lazy = 'dynamic')
 
    def __init__(self, name, capital, numparks, largestParkId, mostRecentEventId, highestPoint,population):

        self.name = name
        self.capital = captital
        self.numparks = numparks
        self.largestParkId = largestParkId
        self.mostRecentEventId = mostRecentEventId
        self.highestPoint = highestPoint
        self.population = population  
 
 
   
    def __repr__(self):
            return '<State %r>' % self.name
 
class Campgrounds(db.Model):
    __tablename__ = 'Campgrounds'

    idnum = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    electricity = db.Column(db.Boolean)
    water = db.Column(db.Boolean)
    sewer = db.Column(db.Boolean)
    pets = db.Column(db.Boolean)
    tents = db.Column(db.Boolean)
    rv_access = db.Column(db.Boolean)
    cabins = db.Column(db.Boolean)

    park_id_fk = db.Column(db.Integer, db.ForeignKey('Parks.idnum'))
    state_id_fk = db.Column(db.Integer, db.ForeignKey('States.idnum')) 
 
    def __init__(self, name, activities, longitude, latitude, address, price, electricity, water, rv_access, tents):
        self.name = name
        self.activities = activities
        self.longitude = longitude
        self.latitude = latitude
        self.address = address
        self.price = price
        self.electricity = electricity
        self.water = water
        self.rv_access = rv_access
        self.tents = tents
   
    def __repr__(self):
            return '<Campgrounds %r>' % self.name