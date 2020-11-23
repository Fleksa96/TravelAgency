import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from app import app
from flask_app import db
from data_layer import Arrangement
from datetime import date


def update_flag_is_active():
    arrangements = db.session.query(Arrangement).\
        filter(Arrangement.end_date < date.today()).\
        all()

    for arrangement in arrangements:
        arrangement.is_active = False


if __name__ == '__main__':
    with app.app_context():
        try:
            update_flag_is_active()
            db.session.commit()
            print("Success!\nFlag is_active has been set!")
        except Exception as e:
            print("Error!\n{}".format(e))
