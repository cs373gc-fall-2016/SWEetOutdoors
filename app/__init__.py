from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/states")
def states():
	return render_template('states.html')

@app.route("/states/texas")
def texas():
	return render_template('/stateInstances/Texas.html')

@app.route("/states/california")
def california():
	return render_template('/stateInstances/California.html')

@app.route("/states/florida")
def florida():
	return render_template('/stateInstances/Florida.html')

@app.route("/parks")
def parks():
	return render_template('parks.html')

@app.route("/parks/BigBend")
def bigBend():
	return render_template('/parkInstances/BigBend.html')

@app.route("/parks/DeathValley")
def deathValley():
	return render_template('/parkInstances/DeathValley.html')

@app.route("/parks/Zilker")
def zilker():
	return render_template('/parkInstances/Zilker.html')






@app.route("/events")
def parks():
	return render_template('events.html')

@app.route("/events/AustinCityLimits")
def bigBend():
	return render_template('/eventInstances/AustinCityLimits.html')

@app.route("/events/YellowStoneAnniversary")
def deathValley():
	return render_template('/eventInstances/YellowStoneAnniversary.html')

@app.route("/events/Relay")
def zilker():
	return render_template('/eventInstances/Relay.html')







if __name__ == "__main__":
	app.run()