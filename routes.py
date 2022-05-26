from flask import Flask
from flask import render_template, redirect, url_for, request

@app.route('/viewevents', methods=['GET'])
def viewevents():
    view_event_form = ViewEvents()
    return render_template('view_events.html', form=view_event_form)

@app.route('/addevent', methods=['GET', 'POST'])
def addevent():
    add_event_form = AddEvent()
    return render_template('add_event.html', form=add_event_form)

@app.route('/updatevent/<name>', methods=['GET', 'POST'])
def updateevent(e_id):
    return null

@app.route('/deletevolunteer/<v_id>', methods=['GET', 'POST'])
def deletevolunteer(v_id):
     return null

@app.route('/deleteevent/<e_id>', methods=['GET', 'POST'])
def deletevent(e_id):
    return null
