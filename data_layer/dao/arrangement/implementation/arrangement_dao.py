from sqlalchemy.exc import SQLAlchemyError

from data_layer.dao.arrangement.arrangement_abstract_dao import \
    ArrangementAbstractDao
from data_layer.models.arrangement import Arrangement

from flask_app import db


class ArrangementDao(ArrangementAbstractDao):

    def get_all_arrangements(self):
        data = db.session.query(Arrangement).all()
        return data

    def create_arrangement(self, data):
        new_arrangement = Arrangement(
            start_date=data['start_date'],
            end_date=data['end_date'],
            description=data['description'],
            destination=data['destination'],
            price=data['price'],
            free_places=data['free_places'],
            admin_id=data['admin_id'],
            tourist_guide_id=data['tourist_guide_id']
        )

        try:
            db.session.add(new_arrangement)
            db.session.commit()
        except SQLAlchemyError as sqlalchemy_error:
            print(f"SqlAlchemy error:: {sqlalchemy_error}")
            return {'message': {sqlalchemy_error}}, 500
        except Exception as error:
            print(f"Unknown error:: {error}")
            return {'message': 'Unknown error.'}, 500

        return new_arrangement
