from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/states/texas")
def texas():
	return render_template('/stateInstances/Texas.html')

@app.route("/states/california")
def california():
	return render_template('/stateInstances/California.html')

if __name__ == "__main__":
	app.run()