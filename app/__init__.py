"""
Main page for routing URL
"""
import os
import requests
from flask import Flask, render_template, request, jsonify
from models import db, State, Event, Campground, Park, app as application
from sqlalchemy import Table, or_, and_
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
    return render_template("test_results.html")


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


@application.route('/orSearch')
def orSearch():
    """
    queries all models and returns matches in both AND and OR format
    """
    search_param = request.args['search']

    # create a list so Big Bend -> [ Big , Bend]
    descriptivename = search_param.split()

    eventsorlist = set()
    statesorlist = set()
    campgroundsorlist = set()
    parksorlist = set()
    orlist = []

    for search in descriptivename:
        print(search)
        park_search_instance = Park.query.filter(or_(Park.name.ilike('%' + search + '%'), Park.latitude.ilike('%' + search + '%'), Park.longitude.ilike('%' + search + '%'), Park.address.ilike('%' + search + '%'), Park.phone.ilike('%' + search + '%'), Park.website.ilike('%' + search + '%'),
                                                     Park.zipcode.ilike('%' + search + '%'), Park.photo_url.ilike('%' + search + '%'), Park.zipregion.ilike('%' + search + '%'), Park.state_fk.ilike('%' + search + '%'))).all()

        for v in park_search_instance:
            parksorlist.add(v)

        event_search_instance = Event.query.filter(or_(Event.latitude.ilike('%' + search + '%'), Event.longitude.ilike('%' + search + '%'), Event.topics.ilike('%' + search + '%'), Event.start_date.ilike('%' + search + '%'), Event.end_date.ilike('%' + search + '%'), Event.pic_url.ilike('%' + search + '%'),
                                                       Event.org_name.ilike('%' + search + '%'), Event.contact_phone_num.ilike('%' + search + '%'), Event.zipregion.ilike('%' + search + '%'), Event.zipcode.ilike('%' + search + '%'))).all()

        for v in event_search_instance:
            eventsorlist.add(v)

        state_search_instance = State.query.filter(or_(State.name.ilike(search), State.description.ilike('%' + search + '%'), State.total_area.ilike(
            '%' + search + '%'), State.population.ilike('%' + search + '%'), State.highest_point.ilike('%' + search + '%'))).all()
        for v in state_search_instance:
            statesorlist.add(v)

        campground_search_instance = Campground.query.filter(or_(Campground.name.ilike('%' + search + '%'), Campground.description.ilike('%' + search + '%'), Campground.latitude.ilike('%' + search + '%'), Campground.longitude.ilike('%' + search + '%'), Campground.direction.ilike('%' + search + '%'),
                                                                 Campground.phone.ilike('%' + search + '%'), Campground.email.ilike('%' + search + '%'), Campground.zipcode.ilike('%' + search + '%'))).all()

        for v in campground_search_instance:
            campgroundsorlist.add(v)
    parkstate = and_(*[Park.state_fk.ilike('%'+s+'%') for s in descriptivename])
    parkurl = and_(*[Park.photo_url.ilike('%'+s+'%') for s in descriptivename])
    parkzipreg = and_(*[Park.zipregion.ilike('%'+s+'%') for s in descriptivename])
    parkzipcode = and_(*[Park.zipcode.ilike('%'+s+'%') for s in descriptivename])
    parkname = and_(*[Park.name.ilike('%'+s+'%') for s in descriptivename]) 
    parklat = and_(*[Park.latitude.ilike('%'+s+'%') for s in descriptivename])
    parklong = and_(*[Park.longitude.ilike('%'+s+'%') for s in descriptivename])
    parkaddress = and_(*[Park.address.ilike('%'+s+'%') for s in descriptivename])
    parkweb = and_(*[Park.website.ilike('%'+s+'%') for s in descriptivename])

    parksand = set()

    thing2 = Park.query.filter(parkname).all()
    thing3 = Park.query.filter(parkurl).all()
    thing4 = Park.query.filter(parkzipreg).all()
    thing5 = Park.query.filter(parkstate).all()
    thing6 = Park.query.filter(parkzipcode).all()
    thing7 = Park.query.filter(parklat).all()
    thing8 = Park.query.filter(parklong).all()
    thing9 = Park.query.filter(parkaddress).all()
    thing10 = Park.query.filter(parkweb).all()

    for stuff in thing2:
        parksand.add(stuff)
    for stuff in thing3:
        parksand.add(stuff)
    for stuff in thing4:
        parksand.add(stuff)
    for stuff in thing5:
        parksand.add(stuff)
    for stuff in thing6:
        parksand.add(stuff)
    for stuff in thing7:
        parksand.add(stuff)
    for stuff in thing8:
        parksand.add(stuff)
    for stuff in thing9:
        parksand.add(stuff)
    for stuff in thing10:
        parksand.add(stuff)


    stateand = set()

    stpop = and_(*[State.population.ilike('%'+s+'%') for s in descriptivename])
    sthigh = and_(*[State.highest_point.ilike('%'+s+'%') for s in descriptivename])
    starea = and_(*[State.total_area.ilike('%'+s+'%') for s in descriptivename])
    stdesc = and_(*[State.description.ilike('%'+s+'%') for s in descriptivename])
    stname = and_(*[State.name.ilike('%'+s+'%') for s in descriptivename]) 

    state1 = State.query.filter(stpop).all()
    state2 = State.query.filter(sthigh).all()
    state3 = State.query.filter(starea).all()
    state4 = State.query.filter(stdesc).all()
    state5 = State.query.filter(stname).all()

    for stuff in state1:
        stateand.add(stuff)
    for stuff in state2:
        stateand.add(stuff)
    for stuff in state3:
        stateand.add(stuff)
    for stuff in state4:
        stateand.add(stuff)
    for stuff in state5:
        stateand.add(stuff)

    eventsand = set()


    eventlat = and_(*[Event.latitude.ilike('%'+s+'%') for s in descriptivename])
    eventlong = and_(*[Event.longitude.ilike('%'+s+'%') for s in descriptivename])
    eventtopics = and_(*[Event.topics.ilike('%'+s+'%') for s in descriptivename])
    eventstart = and_(*[Event.start_date.ilike('%'+s+'%') for s in descriptivename])
    eventend = and_(*[Event.end_date.ilike('%'+s+'%') for s in descriptivename])
    eventpic = and_(*[Event.pic_url.ilike('%'+s+'%') for s in descriptivename])
    eventorg = and_(*[Event.org_name.ilike('%'+s+'%') for s in descriptivename])
    eventphone = and_(*[Event.contact_phone_num.ilike('%'+s+'%') for s in descriptivename])
    eventzipreg = and_(*[Event.zipregion.ilike('%'+s+'%') for s in descriptivename])
    eventzipcode = and_(*[Event.zipcode.ilike('%'+s+'%') for s in descriptivename])

    event1 = Event.query.filter(eventlat).all()
    event2 = Event.query.filter(eventlong).all()
    event3 = Event.query.filter(eventtopics).all()
    event4 = Event.query.filter(eventstart).all()
    event5 = Event.query.filter(eventend).all()
    event6 = Event.query.filter(eventpic).all()
    event7 = Event.query.filter(eventorg).all()
    event8 = Event.query.filter(eventphone).all()
    event9 = Event.query.filter(eventzipreg).all()
    event10 = Event.query.filter(eventzipcode).all()

    for stuff in event1:
        eventsand.add(stuff)
    for stuff in event2:
        eventsand.add(stuff)
    for stuff in event3:
        eventsand.add(stuff)
    for stuff in event4:
        eventsand.add(stuff)
    for stuff in event5:
        eventsand.add(stuff)
    for stuff in event6:
        eventsand.add(stuff)
    for stuff in event7:
        eventsand.add(stuff)
    for stuff in event8:
        eventsand.add(stuff)
    for stuff in event9:
        eventsand.add(stuff)
    for stuff in event10:
        eventsand.add(stuff)

    campname = and_(*[Campground.name.ilike('%'+s+'%') for s in descriptivename])
    campdescript = and_(*[Campground.description.ilike('%'+s+'%') for s in descriptivename])
    camplat = and_(*[Campground.latitude.ilike('%'+s+'%') for s in descriptivename])
    camplong = and_(*[Campground.longitude.ilike('%'+s+'%') for s in descriptivename])
    campdirect = and_(*[Campground.direction.ilike('%'+s+'%') for s in descriptivename])
    campphone = and_(*[Campground.phone.ilike('%'+s+'%') for s in descriptivename])
    campemail = and_(*[Campground.email.ilike('%'+s+'%') for s in descriptivename])
    campzip = and_(*[Campground.zipcode.ilike('%'+s+'%') for s in descriptivename])

    camp1 = Campground.query.filter(campname).all()
    camp2 = Campground.query.filter(campdescript).all()
    camp3 = Campground.query.filter(camplat).all()
    camp4 = Campground.query.filter(camplong).all()
    camp5 = Campground.query.filter(campdirect).all()
    camp6 = Campground.query.filter(campphone).all()
    camp7 = Campground.query.filter(campemail).all()
    camp8 = Campground.query.filter(campzip).all()

    campsand = set()

    for stuff in camp1:
        campsand.add(stuff)
    for stuff in camp2:
        campsand.add(stuff)
    for stuff in camp3:
        campsand.add(stuff)
    for stuff in camp4:
        campsand.add(stuff)
    for stuff in camp5:
        campsand.add(stuff)
    for stuff in camp6:
        campsand.add(stuff)
    for stuff in camp7:
        campsand.add(stuff)
    for stuff in camp8:
        campsand.add(stuff)


    return render_template('Search.html', eventsorlist=eventsorlist, statesorlist=statesorlist, campgroundsorlist=campgroundsorlist, parksorlist=parksorlist, parksandlist=parksand, statesandlist=stateand, campgroundsandlist=campsand, search=search_param)

    #print("before the or code")
    # print parksorlist
    # print eventsorlist
    # print statesorlist
    # print campgroundsorlist


@application.route('/visualization')
def visualization():
    """
    route to the visualization page for PartyPeople's API
    """
    return render_template('visualization.html')

if __name__ == '__main__':
    """
    main method to run program
    """
    application.debug = True
    application.run(threaded=True)
