from data_layer.dao.arrangement.arrangement_abstract_dao import \
    ArrangementAbstractDao
from data_layer.models.arrangement import Arrangement
from data_layer.models.user import users_arrangements, User

from flask_app import db


class ArrangementDao(ArrangementAbstractDao):

    def get_users_from_reservation(self, arrangement_id):
        users = db.session.query(User,
                                 Arrangement. \
                                 destination.label('destination')). \
            filter(users_arrangements.c.arrangement_id == arrangement_id). \
            filter(users_arrangements.c.user_id == User.id). \
            all()
        return users

    def delete_arrangement(self, arrangement_id):
        db.session.query(Arrangement). \
            filter(Arrangement.id == arrangement_id). \
            delete()
        db.session.commit()
        return {'message': 'You successfully deleted an arrangement'}, 200

    def get_arrangement_by_id(self, arrangement_id):
        data = db.session.query(Arrangement). \
            filter(Arrangement.id == arrangement_id). \
            first()
        return data

    def get_all_arrangements(self):
        data = db.session.query(Arrangement).all()
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
