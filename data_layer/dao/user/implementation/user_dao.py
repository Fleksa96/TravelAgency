from sqlalchemy.exc import SQLAlchemyError

from data_layer.dao.user.user_abstract_dao import UserAbstractDao
from flask_app import db
from data_layer.models.user import User


class UserDao(UserAbstractDao):

    def create_user(self, user):
        new_user = User(
            first_name=user['first_name'],
            last_name=user['last_name'],
            username=user['username'],
            password=user['password'],
            email=user['email']
        )

        db.session.add(new_user)
        db.session.commit()

        return new_user

    def get_user_by_username(self, username):
        data = db.session.query(User).\
            filter(User.username == username).\
            one_or_none()
        return data

    def get_user_by_email(self, email):
        data = db.session.query(User).\
            filter(User.email == email).\
            one_or_none()
        return data

    def check_identity(self, data):
        user = db.session.query(User).\
                filter(User.username == data['username']).\
                filter(User.password == data['password']).\
                first()
        return user
