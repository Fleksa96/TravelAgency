from flask_restplus import Resource
from flask import request

from flask_app.homepage_blueprint import homepage_api
from flask_app.homepage_blueprint.schemas import \
    GetArrangementSchema, CreateUserSchema, UserSchema, UserLoginSchema
from flask_app.homepage_blueprint.services import \
    UserService, ArrangementService

#schemas
create_user_schema = CreateUserSchema()
user_schema = UserSchema()
user_login_schema = UserLoginSchema()

#services
user_service = UserService()
arrangement_service = ArrangementService()

@homepage_api.route('')
class GetArrangement(Resource):
    def get(self):
        data = arrangement_service.get_all_arrangements()
        print(data)
        arrangements = GetArrangementSchema(many=True).dump(data)
        return arrangements


@homepage_api.route('/registration')
class UserRegistration(Resource):
    def post(self):
        post_data = create_user_schema.load(request.json)
        new_user = user_service.create_new_tourist(user=post_data)
        return user_schema.dump(new_user)


@homepage_api.route('/login')
class UserLogin(Resource):
    def post(self):
        post_data = user_login_schema.load(request.json)
        user = user_service.login_user(data=post_data)
        return user_schema.dump(user)
