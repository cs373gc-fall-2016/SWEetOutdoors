from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
 
 
 
class Parks(db.Model):
    __tablename__ = 'Parks'
    idnum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    opentime = db.Column(db.Integer)
    closetime = db.Column(db.Integer)
    website = db.Column(db.String)
 
    eventId = db.Column(db.Integer, db.ForeignKey('Events.idnum'))
    events = db.relationship('Events', backref = 'Parks', lazy = 'dynamic')

    
    states = db.relationship('States', backref = 'Parks', lazy = 'dynamic')

    campgroundId = db.Column(db.Integer, db.ForeignKey('Campgrounds.idnum'))
    campgrounds = db.relationship('Campgrounds', backref = 'Parks', lazy = 'dynamic')
 
    def __init__(self, name, activities, campground, price, opentime, closetime, website):
        self.name = name
        self.activities = activities
        self.campground = campground
        self.price = price
        self.opentime = opentime
        self.closetime = closetime
        self.website = website
 
    def __repr__(self):
            return '<Park %r>' % self.name
 
class Events(db.Model):
    __tablename__ = 'Events'
 
    idnum = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    startDate = db.Column(db.String)# may need to change
    email = db.Column(db.String)
    url = db.Column(db.String)
    city = db.Column(db.String)
    #activities = db.Column(db.String,foreign_key = True) #navigates to activity
 
    parkId = db.Column(db.Integer, db.ForeignKey('Parks.idnum'))
    parks = db.relationship('Parks', backref = 'Events', lazy = 'dynamic')

    stateId = db.Column(db.Integer, db.ForeignKey('States.idnum'))
    states = db.relationship('States', backref = 'Events', lazy = 'dynamic')
 
    def __init__(self, email, name, startDate, category, url, park, city, state):
        self.email = email
        self.name = name
        self.startDate = startDate
        self.category = category
        self.url = url
        self.park = park
        self.city = city
        self.state = state
 
 
 
    def __repr__(self):
            return '<Event %r>' % self.name
 

class States(db.Model):
    __tablename__ = 'States'
    idnum = db.Column(db.Integer, primary_key = True)
    numparks = db.Column(db.Integer)
    name = db.Column(db.String)
    highestPoint = db.Column(db.String)
    population = db.Column(db.Integer)
    capital = db.Column(db.String)
    #largestPark = db.Column(db.String)
    #mostRecentEvent = db.Column(db.String)
    #highestPointNum
    #terrain
    #safety concerns
 
    largestParkId = db.Column(db.Integer, db.ForeignKey('Parks.idnum'))

    mostRecentEventId = db.Column(db.Integer, db.ForeignKey('Events.idnum'))
    events = db.relationship('Events', backref = 'States', lazy = 'dynamic')

    campgrounds = db.relationship('Campgrounds', backref = 'States', lazy = 'dynamic')
 
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
    name = db.Column(db.String)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    address = db.Column(db.Float)
    price = db.Column(db.Float)
    electricity = db.Column(db.Boolean)
    water = db.Column(db.Boolean)
    rv_access = db.Column(db.Boolean)
    tents = db.Column(db.Boolean)

    parkId = db.Column(db.Integer, db.ForeignKey('Parks.idnum'))
    stateId = db.Column(db.Integer, db.ForeignKey('States.idnum'))
 
    parks = db.relationship('Parks', backref = 'Campgrounds', lazy = 'dynamic')
 
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
 
