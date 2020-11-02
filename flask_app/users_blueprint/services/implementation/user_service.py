from flask_app.users_blueprint.services.user_abstract_service import \
    UserAbstractService
from data_layer import UserDao, User

from flask_app.common_blueprint.services import GenericService

from werkzeug.exceptions import Conflict

# daos
user_dao = UserDao()


class UserService(GenericService, UserAbstractService):

    @staticmethod
    def _check_if_arrangement_exist(arrangement_id):
        arrangement = GenericService.check_if_arrangement_exist(
            arrangement_id=arrangement_id
        )
        return arrangement

    @staticmethod
    def _check_if_username_is_unique(username):
        user = user_dao.get_user_by_username(username=username)
        if user:
            raise Conflict(description='Username is not unique!')

    @staticmethod
    def _check_if_email_is_unique(email):
        user = user_dao.get_user_by_email(email=email)
        if user:
            raise Conflict(description='Email is not unique!')

    @staticmethod
    def _check_if_username_exist(username):
        user = user_dao.get_user_by_username(username=username)
        if not user:
            raise Conflict(description='Username does not exist!')

    @staticmethod
    def _check_password_for_username(data):
        user = user_dao.check_identity(username=data.get('username'), \
                                       password=data.get('password'))
        if not user:
            raise Conflict(description='Wrong password!')
        return user

    def create_new_tourist(self, post_data):
        new_user = User(
            first_name=post_data.get('first_name'),
            last_name=post_data.get('last_name'),
            username=post_data.get('username'),
            password=post_data.get('password'),
            email=post_data.get('email')
        )
        self._check_if_username_is_unique(username=new_user. \
                                          username. \
                                          strip())

        self._check_if_email_is_unique(email=new_user. \
                                       email. \
                                       strip())

        new_user = user_dao.create_user(new_user=new_user)
        return new_user

    def login_user(self, data):
        self._check_if_username_exist(username=data. \
                                      get('username'). \
                                      strip())

        user = self._check_password_for_username(data=data)
        return user

    def get_all_travel_guides_without_arrangement(self, arrangement_id):
        arrangement = self.check_if_arrangement_exist(
            arrangement_id=arrangement_id
        )
        free_guides = user_dao.get_all_travel_guides_without_any_arrangement()
        guides = user_dao.get_all_travel_guides_with_spare_time(
            arrangement=arrangement
        )
        return guides + free_guides

    def get_all_travel_guides_with_application(self, arrangement_id):
        arrangement = self.check_if_arrangement_exist(
            arrangement_id=arrangement_id
        )
        guides = user_dao.get_all_travel_guides_with_application(
            arrangement=arrangement
        )
        return guides
