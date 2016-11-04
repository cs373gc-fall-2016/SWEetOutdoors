"""
Unit tests for our database
"""
from models import Park, State, Campground, Event
import unittest
from flask import Flask 
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
db = SQLAlchemy(app)

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

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def setUp(self):
        db.create_all()

    # parks
    def test_park(self):
        park = Park("Park","13.87","125.64","2419 Rio Grande", "(555)-555-5555","3.5","google.com","78705","google.com","787","Texas")
        db.session.add(park)
        db.session.commit()
        parks = Park.query.all()
        self.assertTrue(park in parks)

    def test_park2(self):
        park = Park("Park2","13.87","125.64","2317 Speedway", "(555)-555-5555","3.5","google.com","78705","google.com","787","Texas")
        db.session.add(park)
        db.session.commit()
        parks = Park.query.all()
        self.assertTrue(park in parks)

    def test_park3(self):
        park = Park("Park3","13.87","125.64","2419 Rio Grande", "(555)-555-5555","3.5","google.com","78705","google.com","787","Texas")
        db.session.add(park)
        db.session.commit()
        parks = Park.query.all()
        self.assertTrue(park in parks)

    # campgrounds 
    def test_campground(self):
        campground = Campground("Camping","tents","45.38","-53.87", "go right", "(555)-555-5555", "contact@gmail.com", "78705")
        db.session.add(campground)
        db.session.commit()
        campgrounds = Campground.query.all()
        self.assertTrue(campground in campgrounds)
    
    def test_campground2(self):
        campground = Campground("Everglades","lodge","145.38","42.45", "go straight", "(555)-555-5555", "contact@gmail.com", "78705")
        db.session.add(campground)
        db.session.commit()
        campgrounds = Campground.query.all()
        self.assertTrue(campground in campgrounds)     

    def test_campground3(self):
        campground = Campground("Yosemite","RVs","46.15","-53.87", "go left", "(555)-555-5555", "contact@gmail.com", "78705")
        db.session.add(campground)
        db.session.commit()
        campgrounds = Campground.query.all()
        self.assertTrue(campground in campgrounds) 

    # states
    def test_state(self):
        state = State("Texas","big","872647","10000000","1234567")
        db.session.add(state)
        db.session.commit()
        states = State.query.all()
        self.assertTrue(state in states)

    def test_state2(self):
        state = State("Florida","panhandle","600000", "105036", "9854432")
        db.session.add(state)
        db.session.commit()
        states = State.query.all()
        self.assertTrue(state in states)  

    def test_state3(self):
        state = State("California","techies","8000000", "125036", "78542")
        db.session.add(state)
        db.session.commit()
        states = State.query.all()
        self.assertTrue(state in states)

    # events
    def test_event(self):
        event = Event("124.56","-26.76","Running","2/5/17", "2/6/17", "google.com","Relay for Life","(555)-555-5555", "Austin","78705","787","Texas")
    	db.session.add(event)
        db.session.commit()
        events = Event.query.all()
        self.assertTrue(event in events)

    def test_event2(self):
        event = Event("124.56","-26.76","Biking","1/1/17", "1/2/17", "google.com","Living Water International","(555)-555-5555", "Austin","78705","787","Texas")
        db.session.add(event)
        db.session.commit()
        events = Event.query.all()
        self.assertTrue(event in events)

    def test_event3(self):
        event = Event("124.56","-26.76","Hiking","2/5/17", "2/6/17", "google.com","Crohns and Colitis Foundation","(555)-555-5555", "Austin","78705","787","Texas")
        db.session.add(event)
        db.session.commit()
        events = Event.query.all()
        self.assertTrue(event in events)

if __name__ == "__main__":
    unittest.main()
