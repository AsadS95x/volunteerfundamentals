from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,IntegerField


class Volform(FlaskForm):
    v_id = IntegerField("Volunteer ID")
    f_name = StringField('First Name')
    l_name = StringField('Last Name')
    Revent = SelectField('Registered Events', choices=[('carwash', 'Car Wash'), ('dinner', 'Dinner'), ('bakesale', 'Bakesale')])
    submit = SubmitField('Register Volunteer')

class UpVolform(FlaskForm):
    f_name = StringField("First Name")
    l_name = StringField("Last Name")
    Revent = SelectField("Revent", choices=[('carwash', 'Car Wash'), ('dinner', 'Dinner'), ('bakesale', 'Bakesale')])
    submit = SubmitField('Update Details')