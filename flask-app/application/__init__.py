from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__, template_folder='templates')

#Using environment variables to hide database and secret key credentials
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SECRET_KEY'] = os.getenv("MY_KEY")
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = 'secretkey'

db = SQLAlchemy(app)

from application import routes

#db.drop_all()
#db.create_all()

