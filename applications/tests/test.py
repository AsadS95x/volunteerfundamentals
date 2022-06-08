from flask import url_for
from flask_testing import TestCase
from applications import app, db
from applications.models import Volunteer, Events

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                #SECRET_KEY='TEST_SECRET_KEY',
                #DEBUG=True,
                #WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        #Adding test volunteer to db
        volunteer1 = Volunteer(f_name="Harry",l_name="Pinero")
        db.session.add(volunteer1)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
