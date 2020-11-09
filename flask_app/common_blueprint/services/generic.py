from data_layer import ArrangementDao, UserDao

from werkzeug.exceptions import Conflict, NotFound

# daos
arrangement_dao = ArrangementDao()
user_dao = UserDao()


class GenericService:

    @staticmethod
    def check_if_user_exist(user_id):
        user = user_dao.get_user_by_id(
            user_id=user_id
        )
        if not user:
            raise NotFound(description='User does not exist!')
        return user

    @staticmethod
    def check_if_arrangement_exist(arrangement_id):
        arrangement = arrangement_dao. \
            get_arrangement_by_id(arrangement_id=arrangement_id)
        if not arrangement:
            raise NotFound(description='Arrangement does not exist!')
        return arrangement

    @staticmethod
    def check_if_user_is_guide(travel_guide_id):
        user = GenericService.check_if_user_exist(
            user_id=travel_guide_id
        )
        if user.user_type != 2:
            raise Conflict(
                description='Travel guide does not exist'
            )
        return user

    @staticmethod
    def check_if_user_is_tourist(tourist_id):
        user = GenericService.check_if_user_exist(
            user_id=tourist_id
        )
        if user.user_type != 3:
            raise Conflict(
                description='Tourist does not exist'
            )
        return user

    @staticmethod
    def get_all_available_travel_guides(arrangement_id):
        arrangement = GenericService.check_if_arrangement_exist(
            arrangement_id=arrangement_id
        )
        free_guides = user_dao.get_all_travel_guides_without_any_arrangement()
        guides = user_dao.get_all_travel_guides_with_spare_time(
            arrangement=arrangement
        )
        return guides + free_guides
