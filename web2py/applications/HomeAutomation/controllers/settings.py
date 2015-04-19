__author__ = 'DragonJujo'
# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def thermostat():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    # response.flash = T("Hello")
    return dict()

def light():
    return dict()


def thermo():
    temps = SQLTABLE(db().select(db.temperatures.ALL), headers='fieldname:capitalize')
    return dict(message=T('GODDAMMIT'), temps=temps)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def form():
    """ a simple entry form with various types of objects """
    form = FORM(TABLE(
        TR('Time:', INPUT(_type='time', _name='timestart',
           requires=IS_TIME('Enter time in the format HH:MM AM')), ''),
        TR(' '),
        TR('Day',
           SELECT('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', _name='dayofweek',
           requires=IS_IN_SET(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])), ''),
        TR(H4('Temperature:'), TD(INPUT(_type='text', _name='temperature',
           requires=IS_INT_IN_RANGE(40, 90, 'Enter a temperature between 40 and 90')), _colspan='2')),
        TR(A(INPUT(_type='button', _value='CANCEL'),
                                                         _href='thermostat.html'), INPUT(_type='submit', _value='SUBMIT')),
    ))
    if form.process().accepted:
        response.flash = 'form accepted'
        tempsetting = db((db.temperatures.day_of_week == form.vars.dayofweek) &
                         (db.temperatures.time_start == form.vars.timestart)).select().first()
        if tempsetting:
            tempsetting.update_record(temperature=form.vars.temperature)
        else:
            db.temperatures.insert(day_of_week=form.vars.dayofweek,
                                   time_start=form.vars.timestart,
                                   temperature=form.vars.temperature)
        redirect(URL('thermostat'))
    elif form.errors:
        response.flash = 'form is invalid'
    else:
        response.flash = 'please fill the form'
    return dict(form=form, vars=form.vars)

def location():
    """
    sets the location for determining home status
    """
    if 'lat' in request.vars:
        geosetting = db((db.geolocation.device == request.vars.device)).select().first()
        if geosetting:
            geosetting.update_record(latitude=request.vars.lat, longitude=request.vars.lng)
        else:
            db.geolocation.insert(device=request.vars.device,
                                  latitude=request.vars.lat,
                                  longitude=request.vars.lng,
                                  home=True)
    return dict()

def form2():
    """ a simple entry form with various types of objects """
    form2 = FORM(TABLE(
        TR('Time:', INPUT(_type='time', _name='time_start',
           requires=IS_TIME('Enter time in the format HH:MM AM'))),
        TR('Day', SELECT('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', _name='day_of_week',
           requires=IS_IN_SET(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']))),
        TR('On or Off:', SELECT('On','Off', _name='status')),
        TR('', INPUT(_type='submit', _value='SUBMIT'))
    ))
    if form2.process().accepted:
        response.flash = 'form accepted'
        lightsetting = db((db.switches.day_of_week == form2.vars.day_of_week) &
                         (db.switches.time_start == form2.vars.time_start)).select().first()
        if lightsetting:
            lightsetting.update_record(status=form2.vars.status)
        else:
            db.switches.insert(day_of_week=form2.vars.day_of_week,
                                   time_start=form2.vars.time_start,
                                   status=form2.vars.status)
        redirect(URL('light'))
    elif form2.errors:
        response.flash = 'form is invalid'
    else:
        response.flash = 'please fill the form'
    return dict(form2=form2, vars=form2.vars)

def room():
    return dict()

def tempcontrol():
    return dict()