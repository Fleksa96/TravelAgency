from flask_app.homepage_blueprint.services.arrangement_abstract_service \
    import ArrangementAbstractService
from data_layer import ArrangementDao

#daos
arrangement_dao = ArrangementDao()


class ArrangementService(ArrangementAbstractService):

    def get_all_arrangements(self):
        data = arrangement_dao.get_all_arrangements()
        return data
