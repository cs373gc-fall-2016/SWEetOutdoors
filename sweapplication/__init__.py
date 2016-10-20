from flask import Flask, render_template, request
application = Flask(__name__)

@application.route("/")
def index():
	return render_template('index.html')

@application.route("/about")
def about():
	return render_template('about.html')

@application.route("/states")
def states():
	return render_template('states.html')

@application.route("/states/texas")
def texas():
	return render_template('/stateInstances/Texas.html')

@application.route("/states/california")
def california():
	return render_template('/stateInstances/California.html')

@application.route("/states/florida")
def florida():
	return render_template('/stateInstances/Florida.html')

@application.route("/parks")
def parks():
	return render_template('parks.html')

@application.route("/parks/BigBend")
def bigBend():
	return render_template('/parkInstances/BigBend.html')

@application.route("/parks/DeathValley")
def deathValley():
	return render_template('/parkInstances/DeathValley.html')

@application.route("/parks/Zilker")
def zilker():
	return render_template('/parkInstances/Zilker.html')

@application.route("/events")
def events():
	return render_template('events.html')

@application.route("/events/AustinCityLimits")
def austinCityLimits():
	return render_template('/eventInstances/AustinCityLimits.html')

@application.route("/events/YellowStoneAnniversary")
def yellowStoneAnniversary():
	return render_template('/eventInstances/YellowStoneAnniversary.html')

@application.route("/events/RunForTheHungry")
def runForTheHungry():
	return render_template('/eventInstances/RunForTheHungry.html')

@application.route("/campgrounds")
def campgrounds():
	return render_template('campgrounds.html')

@application.route("/campgrounds/BearCreek")
def bearCreek():
	return render_template('campgroundInstances/BearCreek.html')

@application.route("/campgrounds/Everglades")
def everglades():
	return render_template('campgroundInstances/Everglades.html')

@application.route("/campgrounds/YosemiteCampground")
def yosemiteCampground():
	return render_template('campgroundInstances/YosemiteCampground.html')