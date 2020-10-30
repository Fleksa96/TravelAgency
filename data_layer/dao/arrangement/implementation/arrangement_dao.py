from sqlalchemy.exc import SQLAlchemyError

from flask_mail import Message

from data_layer.dao.arrangement.arrangement_abstract_dao import \
    ArrangementAbstractDao
from data_layer.models.arrangement import Arrangement
from data_layer.models.user import users_arrangements, User

from flask_app import db, mail


class ArrangementDao(ArrangementAbstractDao):

    def send_email_of_cancellation(self, data):
        arrangement_id = data

        users = db.session.query(User,
                                 Arrangement. \
                                 destination.label('destination')). \
            filter(users_arrangements.c.arrangement_id == arrangement_id). \
            filter(users_arrangements.c.user_id == User.id). \
            all()
        if len(users) > 0:
            msg = Message('Cancellation',
                          sender='lovacportal.podrska@gmail.com',
                          recipients=[u.User.email for u in users])

            msg.body = f'You arrangement {users[0].destination} ' \
                       f'has been cancelled.'
            mail.send(msg)

    def delete_arrangement(self, data):
        arrangement_id = data

        try:
            arrangement = db.session.query(Arrangement). \
                filter(Arrangement.id == arrangement_id). \
                delete()
            db.session.commit()
        except SQLAlchemyError as sqlalchemy_error:
            print(f"SqlAlchemy error:: {sqlalchemy_error}")
            return {'message': {sqlalchemy_error}}, 500
        except Exception as error:
            print(f"Unknown error:: {error}")
            return {'message': 'Unknown error.'}, 500

        return {'message': 'You successfully deleted an arrangement'}, 200

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
            tourist_guide_id=data.get('tourist_guide_id')
        )

        db.session.add(new_arrangement)
        db.session.commit()

        return new_arrangement
