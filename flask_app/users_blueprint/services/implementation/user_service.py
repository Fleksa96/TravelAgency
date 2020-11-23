from flask_app.users_blueprint.services.user_abstract_service import \
    UserAbstractService
from flask_app.common_blueprint.services import GenericService

from data_layer import UserDao, User, ArrangementDao, ReservationDao

from werkzeug.exceptions import Conflict

# daos
user_dao = UserDao()
arrangement_dao = ArrangementDao()
reservation_dao = ReservationDao()

USER_TYPE = ['user_type']


class UserService(GenericService, UserAbstractService):

    @staticmethod
    def _make_user(post_data):
        new_user = User(
            first_name=post_data.get('first_name'),
            last_name=post_data.get('last_name'),
            username=post_data.get('username'),
            password=post_data.get('password'),
            email=post_data.get('email'),
            user_type=post_data.get('user_type')
        )

        new_user = user_dao.create_user(new_user=new_user)
        return new_user

    @staticmethod
    def _check_if_received_data_is_invalid(keys):
        if set(keys).intersection(set(USER_TYPE)):
            raise Conflict(
                description='Only admin can choose user type, '
                            'default is tourist'
            )

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

    def create_new_user(self, post_data, current_user):
        self.check_if_user_is_admin(current_user.id)
        self._check_if_username_is_unique(
            username=post_data.get('username').strip()
        )
        self._check_if_email_is_unique(
            email=post_data.get('email').strip()
        )
        new_user = self._make_user(
            post_data=post_data
        )
        return new_user

    def registration_of_new_user(self, post_data):
        self._check_if_received_data_is_invalid(
            keys=post_data.keys()
        )
        self._check_if_username_is_unique(
            username=post_data.get('username').strip()
        )
        self._check_if_email_is_unique(
            email=post_data.get('email').strip()
        )
        new_user = self._make_user(
            post_data=post_data
        )
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

    def get_all_reservations_for_tourist(self, tourist_id):
        self.check_if_user_is_tourist(
            tourist_id=tourist_id
        )
        arrangements = reservation_dao.get_all_reservations_for_tourist(
            user_id=tourist_id
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
        user = self.check_if_user_exist(
            user_id=user_id
        )
        return user

    def update_user(self, user_id, data):
        user = self.check_if_user_exist(
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
            updated_user=user
        )
        return updated_user

