from flask_app.homepage_blueprint.services.user_abstract_service import \
    UserAbstractService
from data_layer import UserDao

# daos
user_dao = UserDao()


class UserService(UserAbstractService):

    def create_new_tourist(self, user):
        new_user = user_dao.create_user(user=user)
        return new_user

    def login_user(self, data):
        user = user_dao.check_identity(data=data)
        return user
