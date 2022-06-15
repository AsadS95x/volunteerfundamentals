import datetime
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Volunteer, Events



class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            SQLALCHEMY_TRACK_MODIFICATIONS = False,
            SECRET_KEY = 'test secret key',
            WTF_CSRF_ENABLED = False
        )
        return app
    
    def setUp(self):
        demo1 = Volunteer(f_name="Charlie", l_name="Chaplain")
        demo2 = Volunteer(f_name="Fei ", l_name="Xin")
        demo3 = Volunteer(f_name="Cat", l_name="Thompson")
        demo4 = Volunteer(f_name="Willie", l_name="Wonka")
        demo5 = Events(name="Marakech 3000", date=datetime.datetime(2022, 11, 10))
        demo6 = Events(name="London 2022", date=datetime.datetime(2022, 5, 6))
        demo7 = Events(name="China", date=datetime.datetime(2022, 11, 27))
        demo8 = Events(name="Glasgow", date=datetime.datetime(2022, 6, 18))   
        db.create_all()
        db.session.add(demo1)
        db.session.add(demo2)
        db.session.add(demo3)
        db.session.add(demo4)
        db.session.add(demo5)
        db.session.add(demo6)
        db.session.add(demo7)
        db.session.add(demo8)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViewHome(TestBase):
    def test_get_home(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Google', response.data)

class TestViewVol(TestBase):
    def test_get_add(self):
        response = self.client.get(url_for('viewvolunteers'))
        self.assert200(response)
        self.assertIn(b'Volunteers will be shown here', response.data)

class TestAddVol(TestBase):
    def test_post_add(self):
        response = self.client.post(url_for('registervolunteer'),
        data = dict(add="Akki"),
        follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Akki', response.data)
'''
class TestDeleteVol(TestBase):
    def test_post_delete(self):
        response = self.client.post(url_for('registervolunteer'),
        data = dict(add="Akki"),
        follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Akki', response.data)
'''