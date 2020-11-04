from flask_app import db

from data_layer.dao.application.application_abstract_dao \
    import ApplicationAbstractDao


class ApplicationDao(ApplicationAbstractDao):

    def create_application(self, application):
        db.session.add(application)
        db.session.commit()
        return application
