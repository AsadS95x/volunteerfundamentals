from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
import os

app = Flask(__name__, template_folder='templates')

#Using environment variables to hide database and secret key credentials
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = os.getenv("MY_KEY")
app.config['SECRET_KEY'] = 'secretkey'

# db = SQLAlchemy(app)

# db.create_all()

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    event = SelectField('Events', choices=[('carwash', 'Car Wash'), ('dinner', 'Dinner'), ('bakesale', 'Bakesale')])
    submit = SubmitField('Add Name')

@app.route('/viewevents', methods=['GET', 'POST'])
def viewevents():
   # view_event_form = ViewEvents()
    return render_template('view_event.html', message="")

'''
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')'''

@app.route('/newvol', methods=['GET', 'POST'])
def registervolunteer():
    message = ""
    volunteerform = BasicForm()

    if request.method == 'POST':
        first_name = volunteerform.first_name.data
        last_name = volunteerform.last_name.data
        event = volunteerform.event.data

        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f'Thank you, {first_name} {last_name}'

    return render_template('regvol.html', volunteerform=volunteerform, message=message)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')
