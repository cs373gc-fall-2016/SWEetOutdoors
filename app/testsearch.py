import os
import requests
from flask import Flask, render_template, request, jsonify
from models import db, State, Event, Campground, Park, app as application
from sqlalchemy import Table, or_ , and_
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

    eventsorlist = set()
    statesorlist = set()
    campgroundsorlist = set()
    parksorlist = set()
    orlist = []

    for search in descriptivename:
        print search
        park_search_instance = Park.query.filter(or_(Park.name.like('%'+search+'%'), Park.latitude.like('%'+search+'%'), Park.longitude.like('%'+search+'%'), Park.address.like('%'+search+'%'), Park.phone.like('%'+search+'%'),Park.website.like('%'+search+'%'),
            Park.zipcode.like('%'+search+'%'), Park.photo_url.like('%'+search+'%'), Park.zipregion.like('%'+search+'%'), Park.state_fk.like('%'+search+'%'))).all()
        
        for v in park_search_instance:
            parksorlist.add(v)


        event_search_instance = Event.query.filter(or_(Event.latitude.like('%'+search+'%'), Event.longitude.like('%'+search+'%'), Event.topics.like('%'+search+'%'), Event.start_date.like('%'+search+'%'), Event.end_date.like('%'+search+'%'), Event.pic_url.like('%'+search+'%'),
                     Event.org_name.like('%'+search+'%'), Event.contact_phone_num.like('%'+search+'%'), Event.zipregion.like('%'+search+'%'), Event.zipcode.like('%'+search+'%'))).all()
        
        for v in event_search_instance:
            eventsorlist.add(v)

        state_search_instance = State.query.filter(or_(State.name.like(search), State.description.like('%'+search+'%'), State.total_area.like('%'+search+'%'), State.population.like('%'+search+'%'), State.highest_point.like('%'+search+'%'))).all()
        for v in state_search_instance:
            statesorlist.add(v)

        
        campground_search_instance = Campground.query.filter(or_(Campground.name.like('%'+search+'%'), Campground.description.like('%'+search+'%'), Campground.latitude.like('%'+search+'%'), Campground.longitude.like('%'+search+'%'), Campground.direction.like('%'+search+'%'), 
            Campground.phone.like('%'+search+'%'), Campground.email.like('%'+search+'%'), Campground.zipcode.like('%'+search+'%'))).all()
        
        for v in campground_search_instance:
            campgroundsorlist.add(v)

    print("before the or code")
    print parksorlist
    print eventsorlist
    print statesorlist
    print campgroundsorlist

    

func("Texas camp park running")