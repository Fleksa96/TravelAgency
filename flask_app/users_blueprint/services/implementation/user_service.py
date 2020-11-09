from flask_app.users_blueprint.services.user_abstract_service import \
    UserAbstractService
from data_layer import UserDao, User, ArrangementDao

from flask_app.common_blueprint.services import GenericService

from werkzeug.exceptions import Conflict

# daos
user_dao = UserDao()
arrangement_dao = ArrangementDao()


class UserService(GenericService, UserAbstractService):

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
        user = user_dao.check_identity(username=data.get('username'),
                                       password=data.get('password'))
        if not user:
            raise Conflict(description='Wrong password!')
        return user

    @staticmethod
    def _check_password_confirmation(password, confirm_password):
        if password != confirm_password:
            raise Conflict(
                description='Password differs from confirmation of password'
            )

    def create_new_tourist(self, post_data):
        new_user = User(
            first_name=post_data.get('first_name'),
            last_name=post_data.get('last_name'),
            username=post_data.get('username'),
            password=post_data.get('password'),
            email=post_data.get('email')
        )
        self._check_if_username_is_unique(
            username=new_user.username.strip()
        )

        self._check_if_email_is_unique(
            email=new_user.email.strip()
        )

        new_user = user_dao.create_user(new_user=new_user)
        return new_user

    def login_user(self, data):
        self._check_if_username_exist(
            username=data.get('username').strip()
        )
        user = self._check_password_for_username(data=data)
        return user

    def get_all_arrangements_for_guide(self, travel_guide_id):
        self.check_if_user_is_guide(
            travel_guide_id=travel_guide_id
        )
        data = arrangement_dao.get_all_arrangements_for_travel_guide(
            travel_guide_id=travel_guide_id
        )
        return data

    def get_all_arrangements_for_tourist(self, tourist_id):
        self.check_if_user_is_tourist(
            tourist_id=tourist_id
        )
        arrangements = arrangement_dao.get_all_arrangements_for_tourist(
            tourist_id=tourist_id
        )
        return arrangements

    def get_all_applications_for_guide(self, travel_guide_id):
        self.check_if_user_is_guide(
            travel_guide_id=travel_guide_id
        )
        data = arrangement_dao.get_all_applications_for_travel_guide(
            travel_guide_id=travel_guide_id
        )
        return data

    def get_user_by_id(self, user_id):
        user = GenericService.check_if_user_exist(
            user_id=user_id
        )
        return user

    def update_user(self, user_id, data):
        user = GenericService.check_if_user_exist(
            user_id=user_id
        )

        if data.get('first_name'):
            user.first_name = data.get('first_name')
        if data.get('last_name'):
            user.last_name = data.get('last_name')
        if data.get('username'):
            self._check_if_username_is_unique(
                username=data.get('username')
            )
            user.username = data.get('username')
        if data.get('email'):
            self._check_if_email_is_unique(
                email=data.get('email')
            )
            user.email = data.get('email')
        if data.get('password'):
            self._check_password_confirmation(
                data.get('password'),
                data.get('confirm_password')
            )
            user.password = data.get('password')

        updated_user = user_dao.update_user_data(
            updated_user=user,
            user_id=user_id
        )
        return updated_user

