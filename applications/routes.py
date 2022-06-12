from applications.models import Volunteer, Events
from applications import app, db
from flask import Flask, redirect, render_template, request, url_for
from applications.forms import UpVolform, Volform,AddEventform, UpEvform


@app.route('/viewevents', methods=['GET'])
def viewevents():
    events = db.session.query(Events).all()
    return render_template('view_events.html', events=events, message="")

@app.route('/addevent', methods=['GET', 'POST'])
def addevent():
    eform = AddEventform()

    if request.method == 'POST': 
        name = eform.name.data
        date = eform.date.data
    #print(" do we reach this?")
        db.session.query(Events).all()
        print(" Break 2")
        add_event = Events( name=name, date=date  )
        print(" Break 3")
        db.session.add(add_event)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template('add_event.html', form=eform)

   
@app.route('/updatevent/<id>', methods=['GET', 'POST'])
def updateevent(id):
    message = "Details Updated"
    event = db.session.query(Events).filter(Events.e_id == id).first()
    UpEform = UpEvform()

    if request.method == 'POST':
        #print ("1: "+request.form['name'])
        event.name = UpEform.name.data
        event.date = UpEform.date.data
        db.session.commit()
        return redirect(url_for("viewevents"))

    return render_template('update_event.html', form=UpEform, message=message)

@app.route('/deleteevent/<id>', methods=['GET', 'POST'])
def deletevent(id):
    message= "Event Removed"
    event = db.session.query(Events).filter(Events.e_id == id)
    #print ("This next line should be the query!")
    event.delete()
    db.session.commit()
    event = db.session.query(Events).all()
    return render_template("view_events.html", events=event, message=message)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')  

@app.route('/viewvols', methods=['GET', 'POST'])
def viewvolunteers():
   #view_event_vform = ViewVolunteers()
    volunteers = db.session.query(Volunteer).all()
    #volunteers = db.session.query(Subjects).all()
    return render_template('view_volunteers.html', volunteers=volunteers, message="")

@app.route('/newvol', methods=['GET', 'POST'])
def registervolunteer():
    message = ""
    vform = Volform()

    if request.method == 'POST':
        #v_id = vform.v_id.data 
        f_name = vform.f_name.data
        l_name = vform.l_name.data
        Revent = vform.Revent.data
        #print(" do we reach this?")
        if len(f_name) == 0 or len(l_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f'Thank you, {f_name} {l_name}'
            db.session.query(Volunteer).all()
            print(" Break 2")
            add_vol = Volunteer( f_name=f_name, l_name=l_name  )
            print(" Break 3")
            db.session.add(add_vol)
            db.session.commit()
            return redirect(url_for("registervolunteer"))

    return render_template('add_vol.html', form=vform, message=message)

@app.route('/delvol/<id>', methods=['GET', 'POST'])
def deletevolunteer(id):
    message= "Volunteer Removed"
    volunteers = db.session.query(Volunteer).filter(Volunteer.v_id == id)
    #print ("This next line should be the query!")
    # #print (volunteers.all())
    volunteers.delete()
    db.session.commit()
    volunteers = db.session.query(Volunteer).all()
    return render_template("view_volunteers.html", volunteers=volunteers, message=message)

@app.route('/updvol/<id>', methods=['GET', 'POST'])
def updatevolunteer(id):
    message = "Details Updated"
    volunteers = db.session.query(Volunteer).filter(Volunteer.v_id == id).first()
    UpVform = UpVolform()

    if request.method == 'POST':
        #print ("2: "+request.form['f_name'])
        #print ("1: "+request.form['l_name'])
        volunteers.f_name = request.form['f_name']
        volunteers.l_name = request.form['l_name']
        db.session.commit()
        return redirect(url_for("viewvolunteers"))

    return render_template('update_vol.html', form=UpVform, message=message)