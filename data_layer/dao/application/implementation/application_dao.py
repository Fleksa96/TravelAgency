from sqlalchemy import desc

from flask_app import db

from data_layer.dao.application.application_abstract_dao \
    import ApplicationAbstractDao
from data_layer.models import Arrangement, User

ACCEPTED = 1
DENIED = 2
ON_HOLD = 3


class ApplicationDao(ApplicationAbstractDao):

    def create_application(self, application):
        db.session.add(application)
        db.session.commit()
        # new_application = db.session.query(guides_applications). \
        #     order_by(desc(guides_applications.c.id)). \
        #     first()
        # return new_application

    def get_application_by_arrangement_user_id(self, user_id, arrangement_id):
        # application = db.session.query(guides_applications). \
        #     filter(guides_applications.c.user_id == user_id). \
        #     filter(guides_applications.c.arrangement_id == arrangement_id). \
        #     one_or_none()
        # return application
        return user_id #obrisi ovo posle

    def update_application_status(self, application, arrangement_id, user_id):
        if application:
            application.request_status = ACCEPTED

        # applications = db.session.query(guides_applications).\
        #     filter(guides_applications.c.user_id != user_id). \
        #     filter(guides_applications.c.arrangement_id == arrangement_id). \
        #     all()
        #
        # for a in applications:
        #     print(a[3])
        #     a[3] = DENIED

        db.session.commit()
