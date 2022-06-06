from applications import db

class Events(db.Model):
    e_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    date = db.Column(db.Date, nullable=False)
    # re = db.relationship('Revents', backref='events') 

class Volunteer(db.Model):
    v_id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    # re = db.relationship('Revents', backref='volunteer')
    re = db.Column(db.String(30), nullable=False)