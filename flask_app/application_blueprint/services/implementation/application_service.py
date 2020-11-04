from werkzeug.exceptions import Conflict

from flask_app.application_blueprint.services.application_abstract_service \
    import ApplicatioAbstractService

from data_layer.dao.arrangement.implementation.arrangement_dao \
    import ArrangementDao
from data_layer.dao.user.implementation.user_dao \
    import UserDao
from data_layer.dao.application.implementation.application_dao \
    import ApplicationDao

from data_layer.models import guides_applications

# daos
arrangement_dao = ArrangementDao()
user_dao = UserDao()
application_dao = ApplicationDao()


class ApplicationService(ApplicatioAbstractService):

    @staticmethod
    def _check_if_arrangement_exist(arrangement_id):
        if not arrangement_id:
            raise Conflict(description='Arrangement does not exist')
        arrangement = arrangement_dao.get_arrangement_by_id(arrangement_id)
        if not arrangement:
            raise Conflict(description='Arrangement does not exist')
        return arrangement

    @staticmethod
    def _check_if_user_exist(user_id):
        if not user_id:
            raise Conflict(description='User does not exist')
        user = user_dao.get_user_by_id(user_id)
        if not user:
            raise Conflict(description='User does not exist')
        return user

    def get_all_arrangements_for_travel_guide(self, travel_guide_id):
        data = arrangement_dao.get_all_arrangements_for_travel_guide(
            travel_guide_id=travel_guide_id
        )
        return data

    def create_application(self, travel_guide_id, post_data):
        arrangement_id = post_data.get('arrangement_id')
        arrangement = self._check_if_arrangement_exist(arrangement_id)
        user = self._check_if_user_exist(travel_guide_id)

        application = arrangement.users_applications.append(user)
        application = application_dao.create_application(
            application=application
        )

        return application






