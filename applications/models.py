from applications import db


enrollment = db.Table( "enrollment",
db.Column("events_id", db.Integer, db.ForeignKey('events.e_id')),
db.Column("volunteer_id", db.Integer, db.ForeignKey('volunteer.v_id'))
)

class Volunteer(db.Model):
    v_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    ''' def __repr__(self):
        return f'<Volunteer: {self.f_name}' '''
  
'''def __init__(self, volunteer_id, events_id):
    self.v_id = volunteer_id
    self.e_id = events_id '''

class Events(db.Model):
    e_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    date = db.Column(db.Date, nullable=False)
    enrollment = db.relationship("Volunteer", secondary=enrollment, backref="assigned", lazy= "select")
    #volunteers= db.relationship("Volunteer", secondary= enrollment)
    '''def __repr__(self):
        return f'<Events: {self.name}' '''