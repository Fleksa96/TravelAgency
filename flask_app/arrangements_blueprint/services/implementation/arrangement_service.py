from werkzeug.exceptions import Conflict

from flask_mail import Message

from datetime import date

from flask_app import mail
from flask_app.arrangements_blueprint.services.arrangement_abstract_service \
    import ArrangementAbstractService

from data_layer.dao.arrangement.implementation.arrangement_dao \
    import ArrangementDao
from data_layer.dao.user.implementation.user_dao import UserDao
from data_layer.models import Arrangement

# daos
arrangement_dao = ArrangementDao()
user_dao = UserDao()


class ArrangementService(ArrangementAbstractService):

    @staticmethod
    def _check_if_arrangement_exist(arrangement_id):
        arrangement = arrangement_dao. \
            get_arrangement_by_id(arrangement_id=arrangement_id)
        if not arrangement:
            raise Conflict(description='Arrangement does not exist!')
        return arrangement

    @staticmethod
    def _check_if_admin_id_is_current_user_id(user_id):
        admin = user_dao.get_user_by_id(
            user_id=user_id
        )
        if admin.admin_id != 1:
            raise Conflict(description='You are not authorized to '
                                       'update this arrangement!')

    @staticmethod
    def _send_email_of_cancellation(arrangement_id):
        users = arrangement_dao. \
            get_users_from_reservation(arrangement_id=arrangement_id)
        if len(users) > 0:
            msg = Message('Cancellation',
                          sender='lovacportal.podrska@gmail.com',
                          recipients=[u.User.email for u in users])

            msg.body = f'You arrangement {users[0].destination} ' \
                       f'has been cancelled.'
            mail.send(msg)

    def get_all_arrangements_for_tourist(self, tourist_id):
        arrangements = arrangement_dao.get_all_arrangements_for_tourist(
            tourist_id=tourist_id
        )
        return arrangements

    def get_arrangement_by_id(self, arrangement_id):
        arrangement = self._check_if_arrangement_exist(
            arrangement_id=arrangement_id
        )
        return arrangement

    def get_all_arrangements(self):
        data = arrangement_dao.get_all_arrangements()
        return data

    def delete_arrangement(self, arrangement_id):
        self._check_if_arrangement_exist(arrangement_id=arrangement_id)
        self._send_email_of_cancellation(arrangement_id=arrangement_id)
        message = arrangement_dao. \
            delete_arrangement(arrangement_id=arrangement_id)
        return message

    def create_arrangement(self, data):
        new_arrangement = Arrangement(
            start_date=data.get('start_date'),
            end_date=data.get('end_date'),
            description=data.get('description'),
            destination=data.get('destination'),
            price=data.get('price'),
            free_places=data.get('free_places'),
            admin_id=data.get('admin_id'),
            travel_guide_id=data.get('travel_guide_id')
        )

        arrangement = arrangement_dao. \
            create_arrangement(new_arrangement=new_arrangement)
        return arrangement

    def update_arrangement(self, id, data):
        arrangement = self._check_if_arrangement_exist(id)

        if data.get('start_date'):
            arrangement.start_date = data.get('start_date')
        if data.get('end_date'):
            arrangement.end_date = data.get('end_date')
        if data.get('tourist_guide_id'):
            arrangement.tourist_guide_id = data.get('travel_guide_id')
        if data.get('free_places'):
            arrangement.free_places = data.get('free_places')
        if data.get('price'):
            arrangement.price = data.get('price')

        arrangement = arrangement_dao. \
            update_arrangement(arrangement=arrangement, id=id)

        return arrangement

    def get_all_arrangements_without_guide(self):
        data = arrangement_dao.get_all_arrangements_without_guide()
        return data

    def get_all_arrangements_for_guide(self, travel_guide_id):
        data = arrangement_dao.get_all_arrangements_for_travel_guide(
            travel_guide_id=travel_guide_id
        )
        return data
