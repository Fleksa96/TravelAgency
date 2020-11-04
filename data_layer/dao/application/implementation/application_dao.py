from sqlalchemy import desc

from flask_app import db

from data_layer.dao.application.application_abstract_dao \
    import ApplicationAbstractDao
from data_layer.models import guides_applications


class ApplicationDao(ApplicationAbstractDao):

    def create_application(self, application):
        db.session.add(application)
        db.session.commit()
        new_application = db.session.query(guides_applications). \
            order_by(desc(guides_applications.c.id)). \
            first()
        return new_application
