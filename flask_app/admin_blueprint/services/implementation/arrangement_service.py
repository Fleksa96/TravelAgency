from flask_app.admin_blueprint.services.arrangement_abstract_service import \
    ArrangementAbstractService

from data_layer.dao.arrangement.implementation.arrangement_dao import \
    ArrangementDao

# daos
arrangement_dao = ArrangementDao()


class ArrangementService(ArrangementAbstractService):

    def create_arrangement(self, data):
        arrangement = arrangement_dao.create_arrangement(data=data)
        return arrangement
