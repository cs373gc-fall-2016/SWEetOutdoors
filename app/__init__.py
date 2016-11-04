"""
Main page for routing URL 
"""
import os
import requests
from flask import Flask, render_template, request
from models import db, State, Event, Campground, Park, app as application
from sqlalchemy import Table, or_
import subprocess

# @route('/get/getallstates')
@application.route("/")
def index():
	"""
	routes to home page
	"""
	return render_template('index.html')

@application.route("/about")
def about():
	"""
	routes to about page
	"""
	return render_template('about.html')

 # STATES-------------------------

@application.route("/states")
def states():
	"""
	routes to states table page
	"""
	states = State.query.all()
	# cur = db.session.execute('select * from States order by name desc')
	# states = cur.fetchall()
	return render_template('states.html', states=states)

@application.route("/state_row", methods =['GET', 'POST'])
def state_row(key, tablename):
	"""
	routes to specific state page
	"""
	state_instance = none
	if(tablename == 'Parks'):
		state_instance = State.query.filter_by(name = key).first()
	return state_instance


@application.route("/states/<name>")
def state_instance(name):
	"""
	routes to specific state page
	"""
	state_instance = State.query.filter_by(name = name).first()
	return render_template('stateInstances/StateTemplate.html', state_instance=state_instance)

@application.route("/states/texas")
def texas():
	"""
	routes to texas page
	"""
	return render_template('/stateInstances/Texas.html')

@application.route("/states/california")
def california():
	"""
	routes to california page
	"""
	return render_template('/stateInstances/California.html')

@application.route("/states/florida")
def florida():
	"""
	routes to florida page
	"""
	return render_template('/stateInstances/Florida.html')


 # PARKS-------------------------
@application.route("/parks", methods=['GET'])
def parks():
	"""
	routes to parks table page
	"""
	parks = Park.query.all()
	return render_template('parks.html', parks=parks)

@application.route("/parks/<idnum>")
def parks_instance(idnum):
	"""
	routes to specific park page
	"""
	park_instance = Park.query.filter_by(idnum = idnum).first()
	return render_template('parkInstances/ParkTemplate.html', park_instance=park_instance)

@application.route("/park_row?key=<key>&tablename=<tablename>")
def park_row(key, tablename):
	"""
	routes to specific park page
	"""
	park_instance = none
	if(tablename == 'States'):
		park_instance = Park.query.filter_by(state_fk = key).first()
	return "asdf"

@application.route("/parks/BigBend")
def bigBend():
	"""
	routes to Big Bend page
	"""
	return render_template('/parkInstances/BigBend.html')

@application.route("/parks/DeathValley")
def deathValley():
	"""
	routes to Death Valley page
	"""
	return render_template('/parkInstances/DeathValley.html')

@application.route("/parks/Zilker")
def zilker():
	"""
	routes to Zilker Park page
	"""
	return render_template('/parkInstances/Zilker.html')

# Event----------------------------------

@application.route("/events")
def events():
	"""
	routes to events table page
	"""
	events = Event.query.all()
	return render_template('events.html', events=events)

@application.route("/events/<idnum>")
def event_instance(idnum):
	"""
	routes to specific state page
	"""
	event_instance = Event.query.filter_by(idnum = idnum).first()
	return render_template('eventInstances/EventTemplate.html', event_instance=event_instance)

@application.route("/events/AustinCityLimits")
def austinCityLimits():
	"""
	routes to Austin City Limits page
	"""
	return render_template('/eventInstances/AustinCityLimits.html')

@application.route("/events/YellowStoneAnniversary")
def yellowStoneAnniversary():
	"""
	routes to YellowStoneAnniversary page
	"""
	return render_template('/eventInstances/YellowStoneAnniversary.html')

@application.route("/events/RunForTheHungry")
def runForTheHungry():
	"""
	routes to run for the hungry page
	"""
	return render_template('/eventInstances/RunForTheHungry.html')

# Campgrounds-----------------------------------------

@application.route("/campgrounds")
def campgrounds():
	"""
	routes to campgrounds table page
	"""
	campgrounds = Campground.query.all()
	return render_template('campgrounds.html', campgrounds=campgrounds)

@application.route("/campgrounds/<idnum>")
def campground_instance(idnum):
	"""
	routes to specific campground page
	"""
	campground_instance = Campground.query.filter_by(idnum = idnum).first()
	return render_template('campgroundInstances/CampgroundTemplate.html', campground_instance=campground_instance)

@application.route("/campgrounds/BearCreek")
def bearCreek():
	"""
	routes to Bear Creek page
	"""
	return render_template('/campgroundInstances/BearCreek.html')

@application.route("/campgrounds/Everglades")
def everglades():
	"""
	routes to Everglades page
	"""
	return render_template('/campgroundInstances/Everglades.html')

@application.route("/campgrounds/YosemiteCampground")
def yosemiteCampground():
	"""
	routes to Yosemite campgrounds page
	"""
	return render_template('/campgroundInstances/YosemiteCampground.html')

@application.route ( '/run_tests')
def tests ():
	try:
		process = subprocess.Popen(['python3', '/var/www/SWEetOutdoors-dev/app/tests.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = process.communicate()
		return str(out) + str(err)
	except Exception as exc:
		return str(exc)
@application.route ( '/api/parks')
def tests ():
    dicty = {}
    for i in Park.query.all():
        dicty["idnum"] = i.idnum
        dicty["name"] = i.name
        dicty["latitude"] = i.latitude
        dicty["longitude"] = i.longitude
        dicty["address"] = i.address
        dicty["phone"] = i.phone
        dicty["rating"] = i.rating
        dicty["website"] = i.website
        dicty["zipcode"] = i.zipcode
        dicty["zipregion"] = i.zipregion
        dicty["photo_url"] = i.photo_url
        dicty["state_fk"] = i.state_fk
    return jsonify(**dicty)
 
@application.route ( '/api/parks/')
def tests ():
    dicty = {}
    i = Park.query.filter_by(idnum = 0).first()
    dicty["idnum"] = i.idnum
    dicty["name"] = i.name
    dicty["latitude"] = i.latitude
    dicty["longitude"] = i.longitude
    dicty["address"] = i.address
    dicty["phone"] = i.phone
    dicty["rating"] = i.rating
    dicty["website"] = i.website
    dicty["zipcode"] = i.zipcode
    dicty["zipregion"] = i.zipregion
    dicty["photo_url"] = i.photo_url
    dicty["state_fk"] = i.state_fk
    return jsonify(**dicty)
 
@application.route ( '/api/states')
def tests ():
    dicty = {}
    for i in State.query.all():
        dicty["name"] = i.name
        dicty["description"] = i.description
        dicty["total_area"] = i.total_area
        dicty["population"] = i.population
        dicty["highest_point"] = i.highest_point
        dicty["url"] = i.url
    return jsonify(**dicty)
 
@application.route ( '/api/states/')
def tests ():
    dicty = {}
    i = State.query.filter_by(idnum = 0).first():
    dicty["name"] = i.name
    dicty["description"] = i.description
    dicty["total_area"] = i.total_area
    dicty["population"] = i.population
    dicty["highest_point"] = i.highest_point
    dicty["url"] = i.url
    return jsonify(**dicty)
 
@application.route ( '/api/campgrounds')
def tests ():
    dicty = {}
    for i in Campground.query.all():
        dicty["idnum"] = i.idnum
        dicty["name"] = i.name
        dicty["description"] = i.description
        dicty["latitude"] = i.latitude
        dicty["longitude"] = i.longitude
        dicty["direction"] = i.direction
        dicty["phone"] = i.phone
        dicty["email"] = i.email
        dicty["zipcode"] = i.zipcode
        dicty["park_fk"] = i.park_fk
        dicty["state_fk"] = i.state_fk
    return jsonify(**dicty)
 
@application.route ( '/api/campgrounds/')
def tests ():
    dicty = {}
    i = Campground.query.filter_by(idnum = 0).first()
    dicty["idnum"] = i.idnum
    dicty["name"] = i.name
    dicty["description"] = i.description
    dicty["latitude"] = i.latitude
    dicty["longitude"] = i.longitude
    dicty["direction"] = i.direction
    dicty["phone"] = i.phone
    dicty["email"] = i.email
    dicty["zipcode"] = i.zipcode
    dicty["park_fk"] = i.park_fk
    dicty["state_fk"] = i.state_fk
    return jsonify(**dicty)
 
@application.route ( '/api/events')
def tests ():
    dicty = {}
    for i in Event.query.all():
        dicty["idnum"] = i.idnum
        dicty["latitude"] = i.latitude
        dicty["longitude"] = i.longitude
        dicty["topics"] = i.topics
        dicty["start_date"] = i.start_date
        dicty["end_date"] = i.end_date
        dicty["pic_url"] = i.pic_url
        dicty["org_name"] = i.org_name
        dicty["contact_phone_num"] = i.contact_phone_num
        dicty["park_fk"] = i.park_fk
        dicty["state_fk"] = i.state_fk
    return jsonify(**dicty)
 
@application.route ( '/api/events')
def tests ():
    dicty = {}
    i = Event.query.filter_by(idnum = 0).first()
    dicty["idnum"] = i.idnum
    dicty["latitude"] = i.latitude
    dicty["longitude"] = i.longitude
    dicty["topics"] = i.topics
    dicty["start_date"] = i.start_date
    dicty["end_date"] = i.end_date
    dicty["pic_url"] = i.pic_url
    dicty["org_name"] = i.org_name
    dicty["contact_phone_num"] = i.contact_phone_num
    dicty["park_fk"] = i.park_fk
    dicty["state_fk"] = i.state_fk
    return jsonify(**dicty)
	
if __name__ == '__main__':
	application.debug = True
	application.run()
