"""
Unit tests for our database
"""
#from models import Park, State, Campground, Event
import unittest
from flask import Flask 
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from testmodels import app, db, Park, State, Campground, Event

# app = Flask(__name__)
# #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/test'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test'
# db = SQLAlchemy(app)

class TestModels(TestCase):
    """ 
    def __init__(self, name, price, opentime, closetime, website,
             zipcode, state_id_fk):
    def __init__(self, name, highestPoint, population, description,
             total_area)
    def __init__(self, name, latitude, longitude, electricity, water,
             sewer, pets, park_id_fk, state_id_fk)
    """

    def create_app(self):
        return app

    def setUp(self):
        pass

    def tearDown(self):
        db.session.remove()
        db.drop_all()


    # parks
    def test_park(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        park = Park("Park","13.87","125.64","2419 Rio Grande", "(555)-555-5555","3.5","google.com","78705","google.com","787","Texas")
        db.session.add(park)
        db.session.commit()
        parks = Park.query.all()
        self.assertTrue(park in parks)
        db.session.commit()
        db.drop_all()

    def test_park2(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        park = Park("Park2","13.87","125.64","2317 Speedway", "(555)-555-5555","3.5","google.com","78705","google.com","787","Texas")
        db.session.add(park)
        db.session.commit()
        parks = Park.query.all()
        self.assertTrue(park in parks)
        db.drop_all()

    def test_park3(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        park = Park("Park3","13.87","125.64","2419 Rio Grande", "(555)-555-5555","3.5","google.com","78705","google.com","787","Texas")
        db.session.add(park)
        db.session.commit()
        parks = Park.query.all()
        self.assertTrue(park in parks)
        db.drop_all()

    # campgrounds 
    def test_campground(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        campground = Campground("Camping","tents","45.38","-53.87", "go right", "(555)-555-5555", "contact@gmail.com", "78705",None)
        db.session.add(campground)
        db.session.commit()
        campgrounds = Campground.query.all()
        self.assertTrue(campground in campgrounds)
        db.drop_all()
    
    def test_campground2(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        campground = Campground("Everglades","lodge","145.38","42.45", "go straight", "(555)-555-5555", "contact@gmail.com", "78705",None)
        db.session.add(campground)
        db.session.commit()
        campgrounds = Campground.query.all()
        self.assertTrue(campground in campgrounds)
        db.drop_all()     

    def test_campground3(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        campground = Campground("Yosemite","RVs","46.15","-53.87", "go left", "(555)-555-5555", "contact@gmail.com", "78705",None)
        db.session.add(campground)
        db.session.commit()
        campgrounds = Campground.query.all()
        self.assertTrue(campground in campgrounds)
        db.drop_all() 

    # states
    def test_state(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        state = State("Texas","big","872647","10000000","1234567")
        db.session.add(state)
        db.session.commit()
        states = State.query.all()
        self.assertTrue(state in states)
        db.drop_all()

    def test_state2(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        state = State("Florida","panhandle","600000", "105036", "9854432")
        db.session.add(state)
        db.session.commit()
        states = State.query.all()
        self.assertTrue(state in states)
        db.drop_all()  

    def test_state3(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        state = State("California","techies","8000000", "125036", "78542")
        db.session.add(state)
        db.session.commit()
        states = State.query.all()
        self.assertTrue(state in states)
        db.drop_all()

    # events
    def test_event(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        event = Event("124.56","-26.76","Running","2/5/17", "2/6/17", "google.com","Relay for Life","(555)-555-5555", "Austin","78705","787","Texas")
    	db.session.add(event)
        db.session.commit()
        events = Event.query.all()
        self.assertTrue(event in events)
        db.drop_all()

    def test_event2(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        event = Event("124.56","-26.76","Biking","1/1/17", "1/2/17", "google.com","Living Water International","(555)-555-5555", "Austin","78705","787","Texas")
        db.session.add(event)
        db.session.commit()
        events = Event.query.all()
        self.assertTrue(event in events)
        db.drop_all()

    def test_event3(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        event = Event("124.56","-26.76","Hiking","2/5/17", "2/6/17", "google.com","Crohns and Colitis Foundation","(555)-555-5555", "Austin","78705","787","Texas")
        db.session.add(event)
        db.session.commit()
        events = Event.query.all()
        self.assertTrue(event in events)
        db.drop_all()

if __name__ == "__main__":
    unittest.main()
