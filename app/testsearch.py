import os
import requests
from flask import Flask, render_template, request, jsonify
from models import db, State, Event, Campground, Park, app as application
from sqlalchemy import Table, or_
import subprocess

def func(search):


    """
    FROM STACKOVERFLOW

    db.users.filter_by(name='Joe')

    The same can be accomplished with filter by writing

    db.users.filter(db.users.name=='Joe')

    but you can also write more powerful queries containing expressions like

    db.users.filter(or_(db.users.name=='Ryan', db.users.country=='England'))
    searching
    """

    descriptivename = search.split() # create a list so Big Bend -> [ Big , Bend]



    #THIS IS THE AND CODE

    park_search_instance = Park.query.filter(or_(Park.name.like('%'+search+'%'), Park.latitude == search, Park.longitude == search, Park.address == search, Park.phone == search,Park.website == search,
        Park.zipcode == search, Park.photo_url == search, Park.zipregion == search, Park.state_fk == search)).all()
    
    event_search_instance = Event.query.filter(or_(Event.latitude == search, Event.longitude == search, Event.topics == search, Event.start_date == search, Event.end_date == search, Event.pic_url == search,
                 Event.org_name == search, Event.contact_phone_num == search, Event.zipregion == search, Event.zipcode == search)).all()

    state_search_instance = State.query.filter(or_(State.name.like(search), State.description == search, State.total_area == search, State.population == search, State.highest_point == search)).all()
    
    campground_search_instance = Campground.query.filter(or_(Campground.name == search, Campground.description == search, Campground.latitude == search, Campground.longitude == search, Campground.direction == search, 
        Campground.phone == search, Campground.email == search, Campground.zipcode == search)).all()



    parks = []
    events = []
    states = []
    campgrounds = []

    for name in descriptivename:
        #This is the OR code
        print name # Individual word of string so Big, then Bend
        park_search_instances = Park.query.filter(or_(Park.name.like('%'+name+'%'), Park.latitude == name, Park.longitude == name, Park.address == name, Park.phone == name,Park.website == name,
        Park.zipcode == name, Park.photo_url == name, Park.zipregion == name, Park.state_fk == name)).all()
        parks+= park_search_instances


        event_search_instances = Event.query.filter(or_(Event.latitude == name, Event.longitude == name, Event.topics == name, Event.start_date == name, Event.end_date == name, Event.pic_url == name,
                 Event.org_name == name, Event.contact_phone_num == name, Event.zipregion == name, Event.zipcode == search)).all()
        events += event_search_instances

        state_search_instances = State.query.filter(or_(State.name.like(name), State.description == name, State.total_area == name, State.population == name, State.highest_point == name)).all()
        states += state_search_instances

        campground_search_instances = Campground.query.filter(or_(Campground.name == name, Campground.description == name, Campground.latitude == name, Campground.longitude == name, Campground.direction == name, 
        Campground.phone == name, Campground.email == name, Campground.zipcode == name)).all()
        campgrounds += campground_search_instances

       
    print "AND"

    print park_search_instance
    print event_search_instance
    print state_search_instance
    print campground_search_instance

    
    print "OR"

    print parks 
    print events 
    print states 
    print campgrounds


    print "Done"

func("Big Bend")    