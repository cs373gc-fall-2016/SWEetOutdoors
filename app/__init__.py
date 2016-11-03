"""
Main page for routing URL 
"""
import os
import requests
from flask import Flask, render_template, request
from models import db, State, app as application
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

@application.route("/states")
def states():
	"""
	routes to states table page
	"""
	states = State.query.all()
	# cur = db.session.execute('select * from States order by name desc')
	# states = cur.fetchall()
	return render_template('states.html', states=states)

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

@application.route("/parks")
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

@application.route("/events")
def events():
	"""
	routes to events table page
	"""
	return render_template('events.html')

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

@application.route("/campgrounds")
def campgrounds():
	"""
	routes to campgrounds table page
	"""
	return render_template('campgrounds.html')

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

if __name__ == '__main__':
	application.debug = True
	application.run()