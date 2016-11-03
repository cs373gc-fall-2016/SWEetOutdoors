"""
Unit tests for our database
"""
from models import Park, State, Campground, Event
import unittest
from models import app
from flask_testing import TestCase

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
        # pass in test configuration
        # app.config['SQLALCHEMY_DATABASE_URI'] = "postresql://"
        #app.config['TESTING'] = True
        # db.create_all()
            return app

	def setUp(self):
       # db.create_all()
            state = State("Texas","GuadalupePeak","big","10000000","1234567")
            event = Event("Relay","Running","2/5/17","relay@gmail.com","relay.com","14553","23","12", "a", "b", "c", "d")
            park = Park("Park","200","1000","2000","",12,"parkwebsite.com","65766","77712", "dkdk", "Texas")
       	    campground = Campground("BearCreek","its a creek", "324.55","367.65","True","False","True",71832, "Texas")
            self.test_group = []
       # self.test_group += [{'event':event, 'park', park, 'state':state, 'campground':campground}]
            self.event = event
            self.park = park
            self.state = state
            self.campground = campground
        
        # park2 = Park("Park3",60,1200,2030,"park3website.com",61261,27)
        # event2 = Event("Bike Fest","Biking","11/3/16","bikefest@gmail.com","bikefest.com",54321,12,18)
        # campground2 = Campground("Yosemite",46.15,142.45,False,False,True,True,17,59)
        # state2 = State("Florida","Mount Tallahasee","105036","crazy","600000")
        # test_group += [dict('event':event2, 'park', park2, 'state':state2, 'campground':campground2)]
        # # self.park2 = park2
        # # self.event2 = event2
        # # self.state2 = state2
        # # self.campground2 = campground2

        # park3 = Park("Park2",50,1030,1930,"park2website.com",60061,14)
        # event3 = Event("Yellowstone Anniversary","Hiking","12/9/16","ys@gmail.com","ys.com",54321,12,18)
        # campground3 = Campground("Everglades",32.15,172.45,True,False,True,True,77,89)
        # state3 = State("California","Mount HippieDippie","1958036","west","800500")
        # test_group += [dict('event':event3, 'park', park3, 'state':state3, 'campground':campground3)]
        # # self.park3 = park3
        # # self.event3 = event3
        # # self.state3 = state3
        # # self.campground3 = campground3

	def tearDown(self):
            db.session.remove()
            db.drop_all()

    # def test_add(self):
    #     try:
    #         db.session.add(blah)
    #         # query for it
    #         # add the next thing

    # def test_state3(self):
    # 	sdict = {'name':'California','highestPoint':'Mount HippieDippie','population':'1958036','description':'west','total_area':'800500'}
    # 	self.assertEqual(self.state3().dictionary(),edict)

    # def test_campground3(self):
    # 	cdict = {name:'Everglades','latitude':'32.15','longitude':'172.45','electricity':'True',
    # 	'water':'False','sewer':'True','pets':'True','park_id_fk':'77','state_id_fk':'89'}
    # 	self.assertEqual(self.campground3().dictionary(),cdict)    

    # def test_event3(self):
    # 	edict = {'name':'Yellowstone Anniversary','category':'Hiking','date':'12/9/16',
    # 	'email':'ys@gmail.com','url':'ys.com','zipcode':'54321','park_id_fk':'12','state_id_fk':'18'}
    # 	self.assertEqual(self.event3().dictionary(),edict)

    # def test_park3(self):
    # 	pdict = {'name': 'Park2', 'price': '50', 'opentime': '1030', 'closetime': '1930',
    # 	'website':'park2website.com','zipcode':'60061','park_id_fk':'14'}
    # 	self.assertEqual(self.park3().dictionary(),pdict)


    # def test_state2(self):
    # 	sdict = {'name':'Florida','highestPoint':'Mount Tallahasee','population':'105036','description':'crazy','total_area':'600000'}
    # 	self.assertEqual(self.state2().dictionary(),edict)

    # def test_campground2(self):
    # 	cdict = {name:'Yosemite','latitude':'46.15','longitude':'142.45','electricity':'False',
    # 	'water':'False','sewer':'True','pets':'True','park_id_fk':'17','state_id_fk':'59'}
    # 	self.assertEqual(self.campground2().dictionary(),cdict)    

    # def test_event2(self):
    # 	edict = {'name':'Bikefest','category':'Biking','date':'11/13/16',
    # 	'email':'bikefest@gmail.com','url':'bikefest.com','zipcode':'54321','park_id_fk':'12','state_id_fk':'18'}
    # 	self.assertEqual(self.event2().dictionary(),edict)

    # def test_park2(self):
    # 	pdict = {'name': 'Park3', 'price': '60', 'opentime': '1200', 'closetime': '2030',
    # 	'website':'park3website.com','zipcode':'61266','park_id_fk':'27'}
    # 	self.assertEqual(self.park2().dictionary(),pdict)


    # def test_park(self):
    # 	pdict = {'name': 'Park', 'price': '200', 'opentime': '1000', 'closetime': '2000',
    # 	'website':'parkswebsite.com','zipcode':'65766','park_id_fk':'12'}
    # 	self.assertEqual(self.park().dictionary(),pdict)

    # def test_event(self):
    # 	edict = {'name':'Relay','category':'Running','date':'2/5/17',
    # 	'email':'relay@gmail.com','url':'relay.com','zipcode':'14553','park_id_fk':'23','state_id_fk':'12'}
    # 	self.assertEqual(self.event().dictionary(),edict)

    def test_state(self):
        sdict = {'name':'Texas','highest_point':'GuadalupePeak','population':'10000000','description':'big','total_area':'1234567'}
        self.assertEqual(self.state.dictionary(),sdict)

    # def test_campground(self):
    # 	cdict = {name:'BearCreek','latitude':'324.55','longitude':'367.65','electricity':'True',
    # 	'water':'False','sewer':'True','pets':'False','park_id_fk':'67','state_id_fk':'82'}
    # 	self.assertEqual(self.campground().dictionary(),cdict)

if __name__ == "__main__":
    unittest.main()
