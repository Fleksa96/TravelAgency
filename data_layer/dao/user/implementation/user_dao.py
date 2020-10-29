from sqlalchemy.exc import SQLAlchemyError

from data_layer.dao.user.user_abstract_dao import UserAbstractDao
from data_layer.models.arrangement import Arrangement
from flask_app import db
from flask_app.homepage_blueprint.models.user import User


class UserDao(UserAbstractDao):

    def create_user(self, user):
        new_user = User(
            first_name=user['first_name'],
            last_name=user['last_name'],
            username=user['username'],
            password=user['password'],
            email=user['email']
        )

        try:
            db.session.add(new_user)
            db.session.commit()
        except SQLAlchemyError as sqlalchemy_error:
            print(f"SqlAlchemy error:: {sqlalchemy_error}")
            return {'message': {sqlalchemy_error}}, 500
        except Exception as error:
            print(f"Unknown error:: {error}")
            return {'message': 'Unknown error.'}, 500

        return new_user

    def check_identity(self, data):
        user = db.session.query(User).\
                filter(User.username == data['username']).\
                filter(User.password == data['password']).\
                first()
        return user
