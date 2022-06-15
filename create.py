from application import app,db
from application.models import Volunteer, Events,enrollment
import datetime

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    demo1 = Volunteer(f_name="Charlie", l_name="Chaplain")
    demo2 = Volunteer(f_name="Fei ", l_name="Xin")
    demo3 = Volunteer(f_name="Cat", l_name="Thompson")
    demo4 = Volunteer(f_name="Willie", l_name="Wonka")

    demo5 = Events(name="Marakech 3000", date=datetime.datetime(2022, 11, 10))
    demo6 = Events(name="London 2022", date=datetime.datetime(2022, 5, 6))
    demo7 = Events(name="China", date=datetime.datetime(2022, 11, 27))
    demo8 = Events(name="Glasgow", date=datetime.datetime(2022, 6, 18))      

    demo5.enrollment.append(demo1)
    demo5.enrollment.append(demo2)
 

    db.session.add(demo1)
    db.session.add(demo2)
    db.session.add(demo3)
    db.session.add(demo4)
    db.session.add(demo5)
    db.session.add(demo6)
    db.session.add(demo7)
    db.session.add(demo8)
    db.session.commit()
    app.run(debug=True, host='0.0.0.0')