from flask_restplus import Resource
from flask import request


from flask_app.common_blueprint.schemas import \
    CreateUserSchema, GetUserSchema, UserLoginSchema

from flask_app.users_blueprint import users_api
from flask_app.users_blueprint.services import \
    UserService

# schemas
create_user_schema = CreateUserSchema()
get_user_schema = GetUserSchema(many=True)
user_login_schema = UserLoginSchema()

# services
user_service = UserService()


@users_api.route('')
class UserRegistration(Resource):
    # user registration
    def post(self):
        post_data = create_user_schema.load(request.json)
        user = user_service.create_new_tourist(post_data=post_data)
        return get_user_schema.dump(user)


@users_api.route('/<int:id>')
class UserGuides(Resource):
    # getting all travel guides without arrangements and
    # travel guides with spare time
    def get(self, id):
        data = user_service.get_all_travel_guides_without_arrangement(
            arrangement_id=id
        )
        travel_guides = get_user_schema.dump(data)
        return travel_guides


@users_api.route('/application/<int:id>')
class UserGuides(Resource):
    # getting all travel guides with application
    # for arrangement_id
    def get(self, id):
        data = user_service.get_all_travel_guides_with_application(
            arrangement_id=id
        )
        travel_guides = get_user_schema.dump(data)
        return travel_guides


@users_api.route('/login')
class UserLogin(Resource):
    # user login
    def post(self):
        post_data = user_login_schema.load(request.json)
        user = user_service.login_user(data=post_data)
        return get_user_schema.dump(user)
