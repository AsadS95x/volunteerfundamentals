from xmlrpc.client import DateTime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,IntegerField, DateTimeField, DateField


class Volform(FlaskForm):
    v_id = IntegerField("Volunteer ID")
    f_name = StringField('First Name')
    l_name = StringField('Last Name')
    Revent = SelectField('Registered Events', choices=[('carwash', 'Car Wash'), ('dinner', 'Dinner'), ('bakesale', 'Bakesale')])
    submit = SubmitField('Register Volunteer')

class UpVolform(FlaskForm):
    f_name = StringField("First Name")
    l_name = StringField("Last Name")
    #Revent = SelectField("Revent", choices=[('carwash', 'Car Wash'), ('dinner', 'Dinner'), ('bakesale', 'Bakesale')])
    submit = SubmitField('Update Details')

class AddEventform(FlaskForm):
    name = StringField('Event Name')
    date = DateField('When is this event?')
    submit = SubmitField('Register Event')

class UpEvform(FlaskForm):
    name = StringField("Event Name")
    date = DateField('When is this event?')
    submit = SubmitField('Update Details')

class Assignform(FlaskForm):
    name = SelectField("Event Name", choices=[])
    f_name= SelectField("Volunteer Names", choices=[])
    submit = SubmitField('Assign to Event')