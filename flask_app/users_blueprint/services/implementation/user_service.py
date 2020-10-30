from flask_app.users_blueprint.services.user_abstract_service import \
    UserAbstractService
from data_layer import UserDao

from werkzeug.exceptions import Conflict

# daos
user_dao = UserDao()


class UserService(UserAbstractService):

    @staticmethod
    def _check_if_username_is_unique(username):
        user = user_dao.get_user_by_username(username=username)
        if user:
            raise Conflict(description='Username is not unique')

    @staticmethod
    def _check_if_email_is_unique(email):
        user = user_dao.get_user_by_email(email=email)
        if user:
            raise Conflict(description='Email is not unique')

    def create_new_tourist(self, user):
        self._check_if_username_is_unique(username=user. \
                                          get('username'). \
                                          strip())

        self._check_if_email_is_unique(email=user. \
                                       get('email'). \
                                       strip())

        new_user = user_dao.create_user(user=user)
        return new_user

    def login_user(self, data):
        user = user_dao.check_identity(data=data)
        return user
