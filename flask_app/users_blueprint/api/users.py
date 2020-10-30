from flask_restplus import Resource
from flask import request

from flask_app.common_blueprint.schemas import \
    CreateUserSchema, UserSchema, UserLoginSchema, \
    GetArrangementSchema

from flask_app.users_blueprint import users_api
from flask_app.users_blueprint.services import \
    UserService

# schemas
create_user_schema = CreateUserSchema()
user_schema = UserSchema()
user_login_schema = UserLoginSchema()

# services
user_service = UserService()


@users_api.route('')
class UserRegistration(Resource):
    def post(self):
        post_data = create_user_schema.load(request.json)
        new_user = user_service.create_new_tourist(user=post_data)
        return user_schema.dump(new_user)


@users_api.route('/login')
class UserLogin(Resource):
    def post(self):
        post_data = user_login_schema.load(request.json)
        user = user_service.login_user(data=post_data)
        return user_schema.dump(user)
