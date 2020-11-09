from sqlalchemy import distinct
from sqlalchemy.orm import aliased

from data_layer.dao.arrangement.arrangement_abstract_dao import \
    ArrangementAbstractDao

from data_layer.models import User, Arrangement, Reservation, Application

from flask_app import db


class ArrangementDao(ArrangementAbstractDao):

    def get_users_from_reservation(self, arrangement_id):
        users = db.session.query(User,
                                 Arrangement. \
                                 destination.label('destination')). \
            filter(Reservation.arrangement_id == arrangement_id). \
            filter(Reservation.user_id == User.id). \
            filter(Arrangement.is_active.is_(True)). \
            all()
        return users

    def get_admin_id_from_arrangement_id(self, arrangement_id):
        arrangement = db.session.query(Arrangement). \
            filter(Arrangement.id == arrangement_id). \
            filter(Arrangement.is_active.is_(True)). \
            first()
        return arrangement.admin_id

    def delete_arrangement(self, arrangement_id):
        arrangement = db.session.query(Arrangement). \
            filter(Arrangement.id == arrangement_id). \
            first()
        arrangement.is_active = False
        db.session.commit()
        return {'message': 'You successfully deleted an arrangement'}, 200

    def get_arrangement_by_id(self, arrangement_id):
        data = db.session.query(Arrangement). \
            filter(Arrangement.id == arrangement_id). \
            filter(Arrangement.is_active.is_(True)). \
            first()
        return data

    def get_all_arrangements(self):
        data = db.session.query(Arrangement). \
            filter(Arrangement.is_active.is_(True)). \
            all()
        return data

    def create_arrangement(self, new_arrangement):
        db.session.add(new_arrangement)
        db.session.commit()
        return new_arrangement

    def update_arrangement(self, arrangement, id):
        updated_arrangement = db.session.query(Arrangement). \
            filter(Arrangement.id == id). \
            first()
        updated_arrangement = arrangement
        db.session.commit()
        return updated_arrangement

    def get_all_arrangements_depending_guide(self, has_travel_guide):
        data = db.session.query(Arrangement). \
            filter(Arrangement.is_active.is_(True))
        if has_travel_guide:
            data = data.\
                filter(Arrangement.travel_guide_id.isnot(None))
        else:
            data = data. \
                filter(Arrangement.travel_guide_id.is_(None))
        return data.all()

    def get_all_arrangements_for_tourist(self, tourist_id):
        arrangements = db.session.query(Arrangement). \
            join(Reservation,
                 Reservation.arrangement_id == Arrangement.id). \
            filter(Reservation.user_id == tourist_id). \
            filter(Arrangement.is_active.is_(True)). \
            all()
        return arrangements

    def get_all_applications_for_travel_guide(self, travel_guide_id):
        arrangement = aliased(Arrangement, name='arrangement')
        data = db.session. \
            query(arrangement,
                  Application.request_status). \
            join(Application,
                 Application.arrangement_id == Arrangement.id). \
            filter(arrangement.is_active.is_(True)). \
            filter(Application.user_id == travel_guide_id)

        return data.all()

    def get_all_arrangements_for_travel_guide(self, travel_guide_id):
        data = db.session.query(Arrangement). \
            filter(Arrangement.travel_guide_id == travel_guide_id). \
            filter(Arrangement.is_active.is_(True))
        return data.all()

    def get_arrangement_by_destination_and_dates(self, new_arrangement):
        arrangement = db.session.query(Arrangement).\
            filter(Arrangement.destination == new_arrangement.destination).\
            filter(Arrangement.start_date == new_arrangement.start_date).\
            filter(Arrangement.end_date == new_arrangement.end_date).\
            one_or_none()
        return arrangement
