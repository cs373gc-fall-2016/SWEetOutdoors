"""
Main page for routing URL
"""
import os
import requests
from flask import Flask, render_template, request, jsonify
from models import db, State, Event, Campground, Park, app as application
from sqlalchemy import Table, or_
import subprocess

# Actual Webpage Routings


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
    return render_template('states.html', states=states)


@application.route("/states/<name>")
def state_instance(name):
    """
    routes to specific state page by name
    """
    state_instance = State.query.filter_by(name=name).first()
    return render_template('StateTemplate.html', state_instance=state_instance)

# PARKS-------------------------


@application.route("/parks", methods=['GET'])
def parks():
    """
    routes to parks table page
    """
    parks = Park.query.all()
    return render_template('parks.html', parks=parks)


@application.route("/parks/<idnum>")
def park_instance(idnum):
    """
    routes to specific park page by IDnum
    """
    park_instance = Park.query.filter_by(idnum=idnum).first()
    return render_template('ParksTemplate.html', park_instance=park_instance)

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
    routes to specific event page by IDnum
    """
    event_instance = Event.query.filter_by(idnum=idnum).first()
    return render_template('EventTemplate.html', event_instance=event_instance)

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
    routes to specific campground page by IDnum
    """
    campground_instance = Campground.query.filter_by(idnum=idnum).first()
    return render_template('CampgroundTemplate.html', campground_instance=campground_instance)


# Test routing-----------------------------------------

@application.route('/run_tests')
def tests():
    """
    show results of unit tests
    """
    return render_template("textFile.html")


# API calls-----------------------------------------

# Parks-----------------------------------------
@application.route('/api/parks')
def api_parks():
    """
    show list of parks in json format
    if state name is specified (format: /api/parks?state_name=<state_name>), list is filtered
    """
    park_lst = list()
    if 'state_name' in request.args:
        query_lst = Park.query.filter_by(
            state_fk=request.args['state_name']).all()
    else:
        query_lst = Park.query.all()

    for i in query_lst:
        dict_obj = {}
        dict_obj["ID"] = i.idnum
        dict_obj["Name"] = i.name
        dict_obj["Photo URL"] = i.photo_url
        park_lst += [dict_obj]
    return jsonify({"Success:": True, "List Of Parks": park_lst})


@application.route('/api/parks/<id>')
def api_park_details(id):
    """
    Show details of a park by ID
    """
    dict_obj = {}
    try:
        i = Park.query.filter_by(idnum=id).first()
        dict_obj["ID"] = i.idnum
        dict_obj["Name"] = i.name
        dict_obj["Latitude"] = i.latitude
        dict_obj["Longitude"] = i.longitude
        dict_obj["Address"] = i.address
        dict_obj["Phone"] = i.phone
        dict_obj["Rating"] = i.rating
        dict_obj["Website"] = i.website
        dict_obj["Zipcode"] = i.zipcode
        dict_obj["Zipcode Region"] = i.zipregion
        dict_obj["Photo URL"] = i.photo_url
        dict_obj["State"] = i.state_fk
    except AttributeError:
        return jsonify({"Success": False})
    return jsonify({"Details": dict_obj, "Success": True})

# States-----------------------------------------


@application.route('/api/states')
def api_states():
    """
    show list of states in json format
    """
    states_lst = list()
    for i in State.query.all():
        dict_obj = {}
        dict_obj["Name"] = i.name
        states_lst += [dict_obj]
    return jsonify({"Success:": True, "List Of States": states_lst})


@application.route('/api/states/<name>')
def api_state_detail(name):
    """
    show details of a specific state by name
    """
    dict_obj = {}
    try:
        i = State.query.filter_by(name=name).first()
        dict_obj["Name"] = i.name
        dict_obj["Description"] = i.description
        dict_obj["Total Area"] = i.total_area
        dict_obj["Population"] = i.population
        dict_obj["Highest Point"] = i.highest_point
        dict_obj["Map URL"] = i.url
    except AttributeError:
        return jsonify({"Success": False})
    return jsonify({"Details": dict_obj, "Success": True})

# Campgrounds-----------------------------------------


@application.route('/api/campgrounds')
def api_campgrounds():
    """
    show list of campgrounds in json format
    """
    camp_lst = list()
    for i in Campground.query.all():
        dict_obj = {}
        dict_obj["ID"] = i.idnum
        dict_obj["Name"] = i.name
        camp_lst += [dict_obj]
    return jsonify({"Success": True, "List Of Campgrounds": camp_lst})


@application.route('/api/campgrounds/<id>')
def api_campground_detail(id):
    """
    show details of a campground by id
    """
    dict_obj = {}
    try:
        i = Campground.query.filter_by(idnum=id).first()
        dict_obj["ID"] = i.idnum
        dict_obj["Name"] = i.name
        dict_obj["Description"] = i.description
        dict_obj["Latitude"] = i.latitude
        dict_obj["Longitude"] = i.longitude
        dict_obj["Direction"] = i.direction
        dict_obj["Phone"] = i.phone
        dict_obj["Email"] = i.email
        dict_obj["Zipcode"] = i.zipcode
        dict_obj["Park ID"] = i.park_fk
        dict_obj["State Name"] = i.state_fk
    except AttributeError:
        return jsonify({"Success": False})
    return jsonify({"Success": True, "Details": dict_obj})

# Events-----------------------------------------


@application.route('/api/events/')
def api_events():
    """
    give list of events in json format
    if park_id is given, list only returns events near that park
    if state_name is given, list only events in that state_instance
    """
    events_lst = list()
    if 'park_id' in request.args:
        query_lst = Event.query.filter_by(
            park_fk=request.args['park_id']).all()
    elif 'state_name' in request.args:
        query_lst = Event.query.filter_by(
            state_fk=request.args['state_name']).all()
    else:
        query_lst = Event.query.all()

    for i in query_lst:
        dict_obj = {}
        dict_obj["ID"] = i.idnum
        dict_obj["org_name"] = i.org_name
        dict_obj["Topics"] = i.topics
        dict_obj["Start Date"] = i.start_date
        events_lst += [dict_obj]
    return jsonify({"Success": True, "List Of Events": events_lst})


@application.route('/api/events/<id>')
def api_event_details(id):
    """
    give details of a specific event, by ID
    """
    dict_obj = {}
    try:
        i = Event.query.filter_by(idnum=id).first()
        dict_obj["ID"] = i.idnum
        dict_obj["Latitude"] = i.latitude
        dict_obj["Longitude"] = i.longitude
        dict_obj["Topics"] = i.topics
        dict_obj["Start Date"] = i.start_date
        dict_obj["End Date"] = i.end_date
        dict_obj["Pic URL"] = i.pic_url
        dict_obj["Name"] = i.org_name
        dict_obj["Phone"] = i.contact_phone_num
        dict_obj["Closest Park ID"] = i.park_fk
        dict_obj["State Name"] = i.state_fk
    except AttributeError:
        return jsonify({"Success": False})
    return jsonify({"Success": True, "Details": dict_obj})

if __name__ == '__main__':
    """
    main method to run program
    """
    application.debug = True
    application.run(threaded=True)
