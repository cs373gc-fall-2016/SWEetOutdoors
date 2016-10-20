from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/texas")
def texas():
	return render_template('templates/texas.html')

