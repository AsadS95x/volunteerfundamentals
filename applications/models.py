from applications import db

Enrollment=db.Table(
    id = db.Column(db.Integer, primary_key=True),
    e_id = db.Column('events_id', db.Integer, db.ForeignKey('events.e_id')),
    v_id = db.Column('volunteer_id', db.Integer, db.ForeignKey('volunteer.v_id'))
    )
    # re = db.Column(db.String(30), nullable=False)
    # enrollment_date = db.Column('Date', db.String(30))

class Volunteer(db.Model):
    v_id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    #enrollment = db.relationship('Enrollment', backref='volunteer')
    # re = db.Column(db.String(30), nullable=False)

class Events(db.Model):
    e_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    date = db.Column(db.Date, nullable=False)
    volunteers= db.relationship("Volunteer", secondary= Enrollment)
    #enrollment = db.relationship('Enrollment', backref='events') 


