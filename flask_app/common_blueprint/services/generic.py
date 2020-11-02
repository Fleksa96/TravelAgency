from data_layer import ArrangementDao

from werkzeug.exceptions import Conflict

# services
arrangement_dao = ArrangementDao()


class GenericService:

    @staticmethod
    def check_if_arrangement_exist(arrangement_id):
        arrangement = arrangement_dao. \
            get_arrangement_by_id(arrangement_id=arrangement_id)
        if not arrangement:
            raise Conflict(description='Arrangement does not exist!')
        return arrangement
