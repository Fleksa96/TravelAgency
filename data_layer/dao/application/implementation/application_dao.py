from sqlalchemy import desc

from flask_app import db

from data_layer.dao.application.application_abstract_dao \
    import ApplicationAbstractDao
from data_layer.models import Arrangement, User, Application

ACCEPTED = 1
DENIED = 2
ON_HOLD = 3


class ApplicationDao(ApplicationAbstractDao):

    def create_application(self, application):
        db.session.add(application)
        db.session.commit()
        new_application = db.session.query(Application). \
            order_by(desc(Application.id)). \
            first()
        return new_application

    def get_application_by_arrangement_user_id(self, user_id, arrangement_id):
        application = db.session.query(Application). \
            filter(Application.user_id == user_id). \
            filter(Application.arrangement_id == arrangement_id). \
            one_or_none()
        return application

    def update_application_status(self, application, arrangement_id, user_id):
        if application:
            application.request_status = ACCEPTED

        applications = db.session.query(Application).\
            filter(Application.user_id != user_id). \
            filter(Application.arrangement_id == arrangement_id). \
            all()

        for a in applications:
            a.request_status = DENIED

        db.session.commit()
