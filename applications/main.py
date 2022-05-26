from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from applications import routes
import os

app = Flask(__name__)

#Using environment variables to hide database and secret key credentials
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv("MY_KEY")

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')