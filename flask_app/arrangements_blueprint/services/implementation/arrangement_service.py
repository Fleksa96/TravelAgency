from flask_app.arrangements_blueprint.services.arrangement_abstract_service \
    import ArrangementAbstractService

from data_layer.dao.arrangement.implementation.arrangement_dao \
    import ArrangementDao

# daos
arrangement_dao = ArrangementDao()


class ArrangementService(ArrangementAbstractService):

    def get_all_arrangements(self):
        data = arrangement_dao.get_all_arrangements()
        return data

    def delete_arrangement(self, data):
        arrangement_dao.send_email_of_cancellation(data=data)
        message = arrangement_dao.delete_arrangement(data=data)
        return message

    def create_arrangement(self, data):
        arrangement = arrangement_dao.create_arrangement(data=data)
        return arrangement
