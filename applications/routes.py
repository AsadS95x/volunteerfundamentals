from applications.models import Volunteer, Events
from applications import app, db
from flask import Flask, redirect, render_template, request, url_for
from applications.forms import Volform

'''
@app.route('/viewevents', methods=['GET'])
def viewevents():
    view_event_vform = ViewEvents()
    return render_template('view_events.html', vform=view_event_vform)

@app.route('/addevent', methods=['GET', 'POST'])
def addevent():
    add_event_vform = AddEvent()
    return render_template('add_event.html', vform=add_event_vform)

@app.route('/updatevent/<name>', methods=['GET', 'POST'])
def updateevent(e_id):
    return null

@app.route('/updatevol/<name>', methods=['GET', 'POST'])
def updateevent(v_id):
    return null


@app.route('/deleteevent/<e_id>', methods=['GET', 'POST'])
def deletevent(e_id):
    return null
'''
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')  

@app.route('/viewvols', methods=['GET', 'POST'])
def viewvolunteers():
   # view_event_vform = ViewVolunteers()
    volunteers = db.session.query(Volunteer).all()
    #volunteers = db.session.query(Subjects).all()
    return render_template('view_volunteers.html', volunteers=volunteers, message="")


@app.route('/newvol', methods=['GET', 'POST'])
def registervolunteer():
    message = ""
    vform = Volform()

    if request.method == 'POST':
       # v_id = vform.v_id.data 
        f_name = vform.f_name.data
        l_name = vform.l_name.data
        Revent = vform.Revent.data
        
        print(" do we reach this?")
        
        if len(f_name) == 0 or len(l_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f'Thank you, {f_name} {l_name}'
            db.session.query(Volunteer).all()
            print(" Break 2")
            add_vol = Volunteer( f_name=f_name, l_name=l_name, re=Revent  )
            print(" Break 3")
            db.session.add(add_vol)
            db.session.commit()
            return redirect(url_for("registervolunteer"))

    return render_template('addvol.html', form=vform, message=message)


@app.route('/delvol/<id>', methods=['GET', 'POST'])
def deletevolunteer(id):
    volunteers = db.session.query(Volunteer).filter(Volunteer.v_id == id)
    #print ("This next line should be the query!")
    # #print (volunteers.all())
    volunteers.delete()
    db.session.commit()
    return redirect(url_for("viewvolunteers"))