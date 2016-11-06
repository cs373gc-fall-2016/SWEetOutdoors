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
	return render_template('parkInstances/ParksTemplate.html', park_instance=park_instance)

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
	
	return render_template("textFile.html")
	#return render_template('tests.out')
	#try:
	#	process = subprocess.Popen(['python', '/var/www/SWEetOutdoors-dev/app/tests.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	#	out, err = process.communicate()
	#	return str(out) + str(err)
	#except Exception as exc:
	#	return str(exc)

# API calls
@application.route ( '/api/parks')
def api_parks ():
	park_lst = list()
    dict_obj = {}
    for i in Park.query.all():
        dict_obj["id"] = i.idnum
        dict_obj["Name"] = i.name
        dict_obj["Latitude"] = i.latitude
        dict_obj["Longitude"] = i.longitude
        dict_obj["Address"] = i.address
        dict_obj["Phone"] = i.phone
        dict_obj["Rating"] = i.rating
        dict_obj["Website"] = i.website
        dict_obj["Zipcode"] = i.zipcode
        dict_obj["Zipcode Region"] = i.zipregion
        dict_obj["Photo Url"] = i.photo_url
        dict_obj["State"] = i.state_fk
        park_lst += dict_obj
    return jsonify({"success:" : True, "list of parks" : park_lst})
 
@application.route ( '/api/parks/')
def tests2 ():
    dict_obj = {}
    i = Park.query.filter_by(idnum = 0).first()
    dict_obj["idnum"] = i.idnum
    dict_obj["name"] = i.name
    dict_obj["latitude"] = i.latitude
    dict_obj["longitude"] = i.longitude
    dict_obj["address"] = i.address
    dict_obj["phone"] = i.phone
    dict_obj["rating"] = i.rating
    dict_obj["website"] = i.website
    dict_obj["zipcode"] = i.zipcode
    dict_obj["zipregion"] = i.zipregion
    dict_obj["photo_url"] = i.photo_url
    dict_obj["state_fk"] = i.state_fk
    return jsonify(**dict_obj)
 
@application.route ( '/api/states')
def tests3 ():
    dict_obj = {}
    for i in State.query.all():
        dict_obj["name"] = i.name
        dict_obj["description"] = i.description
        dict_obj["total_area"] = i.total_area
        dict_obj["population"] = i.population
        dict_obj["highest_point"] = i.highest_point
        dict_obj["url"] = i.url
    return jsonify(**dict_obj)
 
@application.route ( '/api/states/')
def tests4 ():
    dict_obj = {}
    i = State.query.filter_by(idnum = 0).first()
    dict_obj["name"] = i.name
    dict_obj["description"] = i.description
    dict_obj["total_area"] = i.total_area
    dict_obj["population"] = i.population
    dict_obj["highest_point"] = i.highest_point
    dict_obj["url"] = i.url
    return jsonify(**dict_obj)
 
@application.route ( '/api/campgrounds')
def tests5 ():
    dict_obj = {}
    for i in Campground.query.all():
        dict_obj["idnum"] = i.idnum
        dict_obj["name"] = i.name
        dict_obj["description"] = i.description
        dict_obj["latitude"] = i.latitude
        dict_obj["longitude"] = i.longitude
        dict_obj["direction"] = i.direction
        dict_obj["phone"] = i.phone
        dict_obj["email"] = i.email
        dict_obj["zipcode"] = i.zipcode
        dict_obj["park_fk"] = i.park_fk
        dict_obj["state_fk"] = i.state_fk
    return jsonify(**dict_obj)
 
@application.route ( '/api/campgrounds/')
def tests6 ():
    dict_obj = {}
    i = Campground.query.filter_by(idnum = 0).first()
    dict_obj["idnum"] = i.idnum
    dict_obj["name"] = i.name
    dict_obj["description"] = i.description
    dict_obj["latitude"] = i.latitude
    dict_obj["longitude"] = i.longitude
    dict_obj["direction"] = i.direction
    dict_obj["phone"] = i.phone
    dict_obj["email"] = i.email
    dict_obj["zipcode"] = i.zipcode
    dict_obj["park_fk"] = i.park_fk
    dict_obj["state_fk"] = i.state_fk
    return jsonify(**dict_obj)
 
@application.route ( '/api/events')
def tests7 ():
    dict_obj = {}
    for i in Event.query.all():
        dict_obj["idnum"] = i.idnum
        dict_obj["latitude"] = i.latitude
        dict_obj["longitude"] = i.longitude
        dict_obj["topics"] = i.topics
        dict_obj["start_date"] = i.start_date
        dict_obj["end_date"] = i.end_date
        dict_obj["pic_url"] = i.pic_url
        dict_obj["org_name"] = i.org_name
        dict_obj["contact_phone_num"] = i.contact_phone_num
        dict_obj["park_fk"] = i.park_fk
        dict_obj["state_fk"] = i.state_fk
    return jsonify(**dict_obj)
 
@application.route ( '/api/events')
def tests8 ():
    dict_obj = {}
    i = Event.query.filter_by(idnum = 0).first()
    dict_obj["idnum"] = i.idnum
    dict_obj["latitude"] = i.latitude
    dict_obj["longitude"] = i.longitude
    dict_obj["topics"] = i.topics
    dict_obj["start_date"] = i.start_date
    dict_obj["end_date"] = i.end_date
    dict_obj["pic_url"] = i.pic_url
    dict_obj["org_name"] = i.org_name
    dict_obj["contact_phone_num"] = i.contact_phone_num
    dict_obj["park_fk"] = i.park_fk
    dict_obj["state_fk"] = i.state_fk
    return jsonify(**dict_obj)
	
if __name__ == '__main__':
	application.debug = True
	application.run()
