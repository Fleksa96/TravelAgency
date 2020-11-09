from flask_app import db

from sqlalchemy import not_, between, and_, distinct

from data_layer.dao.user.user_abstract_dao import UserAbstractDao
from data_layer.models import User, Arrangement, Application


class UserDao(UserAbstractDao):

    def get_all_travel_guides_without_any_arrangement(self):
        subquery = db.session.query(Arrangement.travel_guide_id). \
            filter(not_(Arrangement.travel_guide_id.is_(None))). \
            subquery()
        free_travel_guides = db.session.query(User). \
            filter(User.user_type == 2). \
            filter(User.id.notin_(subquery)). \
            all()
        return free_travel_guides

    def get_all_travel_guides_with_application(self, arrangement):
        guides_id = db.session.query(Application.user_id). \
            filter(arrangement.id == Application.arrangement_id). \
            all()

        guides = db.session.query(User). \
            join(Arrangement, Arrangement.travel_guide_id == User.id). \
            filter(User.id.in_(guides_id)). \
            filter(not_(and_(Arrangement.start_date.between(
            arrangement.start_date,
            arrangement.end_date),
            Arrangement.end_date.between(
                arrangement.start_date,
                arrangement.end_date)))). \
            filter(not_(and_(arrangement.start_date > Arrangement.start_date,
                             arrangement.start_date < Arrangement.end_date))).\
            filter(not_(and_(arrangement.end_date > Arrangement.start_date,
                             arrangement.end_date < Arrangement.end_date))). \
            all()

        return guides

    def get_all_travel_guides_with_spare_time(self, arrangement):
        guides = db.session.query(User). \
            join(Arrangement, Arrangement.travel_guide_id == User.id). \
            filter(User.user_type == 2). \
            filter(not_(and_(Arrangement.start_date.between(
            arrangement.start_date,
            arrangement.end_date),
            Arrangement.end_date.between(
                arrangement.start_date,
                arrangement.end_date)))). \
            filter(not_(and_(arrangement.start_date > Arrangement.start_date,
                             arrangement.start_date < Arrangement.end_date))). \
            filter(not_(and_(arrangement.end_date > Arrangement.start_date,
                             arrangement.end_date < Arrangement.end_date))). \
            all()

        return guides

    def create_user(self, new_user):
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def get_user_by_username(self, username):
        data = db.session.query(User). \
            filter(User.username == username). \
            one_or_none()
        return data

    def get_user_by_id(self, user_id):
        data = db.session.query(User). \
            filter(User.id == user_id). \
            one_or_none()
        return data

    def get_user_by_email(self, email):
        data = db.session.query(User). \
            filter(User.email == email). \
            one_or_none()
        return data

    def check_identity(self, username, password):
        user = db.session.query(User). \
            filter(User.username == username). \
            filter(User.password == password). \
            first()
        return user

    def update_user_data(self, updated_user, user_id):
        user = db.session.query(User). \
            filter(User.id == user_id). \
            first()
        user = updated_user
        db.session.commit()
        return user
