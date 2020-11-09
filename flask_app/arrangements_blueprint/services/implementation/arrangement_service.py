from werkzeug.exceptions import Conflict

from flask_mail import Message

from datetime import date

from flask_app import mail
from flask_app.arrangements_blueprint.services.arrangement_abstract_service \
    import ArrangementAbstractService
from flask_app.common_blueprint.services import GenericService

from data_layer.dao.arrangement.implementation.arrangement_dao \
    import ArrangementDao
from data_layer.dao.user.implementation.user_dao import UserDao
from data_layer.dao.application.implementation.application_dao import \
    ApplicationDao

from data_layer.models import Arrangement, Application

# daos
arrangement_dao = ArrangementDao()
user_dao = UserDao()
application_dao = ApplicationDao()


class ArrangementService(ArrangementAbstractService, GenericService):

    @staticmethod
    def _check_if_application_already_exist(user_id, arrangement_id):
        application = application_dao.get_application_by_arrangement_user_id(
            user_id=user_id,
            arrangement_id=arrangement_id
        )
        if application:
            raise Conflict(
                description='Application already exists'
            )

    @staticmethod
    def _update_application_status(user_id, arrangement_id):
        application = application_dao.get_application_by_arrangement_user_id(
            user_id=user_id,
            arrangement_id=arrangement_id
        )
        application_dao.update_application_status(
            application=application,
            arrangement_id=arrangement_id,
            user_id=user_id
        )

    @staticmethod
    def _check_if_guide_is_available(arrangement_id, user):
        guide_ids = \
            GenericService.get_all_available_travel_guides(
                arrangement_id=arrangement_id
            )
        if user not in guide_ids:
            raise Conflict(
                description='Travel guide is occupied'
            )

    @staticmethod
    # flag is used to determine the error message
    # first date is either now() or start_date from arrangement\
    # second date is either new start_date or new end_date
    def _check_if_date_is_invalid(first_date, second_date, flag):
        if first_date > second_date and flag:
            raise Conflict(
                description='Start date is in the past'
            )
        elif first_date > second_date:
            raise Conflict(
                description='Start date is after end date'
            )

    @staticmethod
    def _check_if_destination_with_same_dates_exist(new_arrangement):
        arrangement = arrangement_dao.get_arrangement_by_destination_and_dates(
            new_arrangement=new_arrangement
        )
        if arrangement:
            raise Conflict(
                description='Arrangement already exists'
            )

    @staticmethod
    def _check_if_number_is_positive(number, flag):
        if number < 0 and flag:
            raise Conflict(
                description='Free places must be positive value'
            )
        elif number < 0:
            raise Conflict(
                description='Price must be positive value'
            )

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
        users = arrangement_dao.get_users_from_reservation(
            arrangement_id=arrangement_id
        )
        if len(users) > 0:
            msg = Message('Cancellation',
                          sender='lovacportal.podrska@gmail.com',
                          recipients=[u.User.email for u in users])

            msg.body = f'You arrangement {users[0].destination} ' \
                       f'has been cancelled.'
            mail.send(msg)

    def get_arrangement_by_id(self, arrangement_id):
        arrangement = self.check_if_arrangement_exist(
            arrangement_id=arrangement_id
        )
        return arrangement

    def get_all_arrangements(self):
        data = arrangement_dao.get_all_arrangements()
        return data

    def delete_arrangement(self, arrangement_id):
        self.check_if_arrangement_exist(
            arrangement_id=arrangement_id
        )
        self._send_email_of_cancellation(
            arrangement_id=arrangement_id
        )
        message = arrangement_dao.delete_arrangement(
            arrangement_id=arrangement_id
        )
        return message

    def create_arrangement(self, data):
        new_arrangement = Arrangement(
            start_date=data.get('start_date'),
            end_date=data.get('end_date'),
            description=data.get('description'),
            destination=data.get('destination'),
            price=data.get('price'),
            free_places=data.get('free_places'),
            admin_id=data.get('admin_id')
        )
        self._check_if_destination_with_same_dates_exist(
            new_arrangement=new_arrangement
        )
        arrangement = arrangement_dao. \
            create_arrangement(new_arrangement=new_arrangement)
        return arrangement

    def update_arrangement(self, id, data):
        arrangement = self.check_if_arrangement_exist(
            arrangement_id=id
        )

        if data.get('start_date') and data.get('end_date'):
            self._check_if_date_is_invalid(
                first_date=data.get('start_date'),
                second_date=data.get('end_date'),
                flag=False
            )
            arrangement.start_date = data.get('start_date')
            arrangement.end_date = data.get('end_date')
        else:
            if data.get('end_date'):
                self._check_if_date_is_invalid(
                    first_date=arrangement.start_date,
                    second_date=data.get('end_date'),
                    flag=False
                )
                arrangement.end_date = data.get('end_date')
            if data.get('start_date'):
                self._check_if_date_is_invalid(
                    first_date=date.today(),
                    second_date=data.get('start_date'),
                    flag=True
                )
                self._check_if_date_is_invalid(
                    first_date=data.get('start_date'),
                    second_date=arrangement.end_date,
                    flag=False
                )
                arrangement.start_date = data.get('start_date')
        if data.get('free_places'):
            self._check_if_number_is_positive(
                number=data.get('free_places'),
                flag=True
            )
            arrangement.free_places = data.get('free_places')
        if data.get('price'):
            self._check_if_number_is_positive(
                number=data.get('price'),
                flag=False
            )
            arrangement.price = data.get('price')
        # this has to be last check,
        # because i need to send object arrangement
        if data.get('travel_guide_id'):
            user = self.check_if_user_is_guide(
                travel_guide_id=data.get('travel_guide_id')
            )
            self._check_if_guide_is_available(
                arrangement_id=id,
                user=user
            )
            arrangement.travel_guide_id = data.get('travel_guide_id')
            self._update_application_status(
                user_id=user.id,
                arrangement_id=id
            )

        arrangement = arrangement_dao.update_arrangement(
            arrangement=arrangement,
            id=id
        )

        return arrangement

    def get_all_arrangements_depending_guide(self, has_travel_guide):
        data = arrangement_dao.get_all_arrangements_depending_guide(
            has_travel_guide=has_travel_guide
        )
        return data

    def create_application(self, travel_guide_id, arrangement_id):
        self.check_if_arrangement_exist(arrangement_id)
        user = self.check_if_user_is_guide(travel_guide_id)
        self._check_if_application_already_exist(
            user_id=travel_guide_id,
            arrangement_id=arrangement_id
        )
        self._check_if_guide_is_available(
            arrangement_id=arrangement_id,
            user=user
        )

        application = Application(
            user_id=travel_guide_id,
            arrangement_id=arrangement_id
        )

        application = application_dao.create_application(
            application=application
        )

        return application

    def get_all_guides_with_application(self, arrangement_id):
        arrangement = self.check_if_arrangement_exist(
            arrangement_id=arrangement_id
        )
        available_guides = self.get_all_available_travel_guides(
            arrangement_id=arrangement_id
        )
        guides = user_dao.get_all_travel_guides_with_application(
            arrangement=arrangement,
            available_guides=available_guides
        )
        return guides
