from flask_restplus import Resource
from flask import request


from flask_app.common_blueprint.schemas import \
    CreateUserSchema, GetUserSchema, UserLoginSchema, GetArrangementSchema,\
    GetGuideArrangementSchema, UpdateUserSchema

from flask_app.users_blueprint import users_api
from flask_app.users_blueprint.services import \
    UserService

# schemas
create_user_schema = CreateUserSchema()
get_user_schema = GetUserSchema(many=True)
user_login_schema = UserLoginSchema()
update_user_schema = UpdateUserSchema()

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
class UserProfileApi(Resource):
    # getting user data
    def get(self, id):
        user = user_service.get_user_by_id(
            user_id=id
        )
        return GetUserSchema().dump(user)

    def patch(self, id):
        post_data = update_user_schema.load(request.json)
        user = user_service.update_user(
            user_id=id,
            data=post_data
        )
        return GetUserSchema().dump(user)


@users_api.route('/<int:id>/my-guides')
class GuideArrangementsApi(Resource):
    # getting all arangements for certain travel guide
    def get(self, id):
        data = user_service.get_all_arrangements_for_guide(
            travel_guide_id=id
        )
        arrangements = GetArrangementSchema(many=True).dump(data)
        return arrangements


@users_api.route('/<int:id>/reservations')
class ArrangementReservationApi(Resource):
    # getting tourist reservation arrangements
    def get(self, id):
        data = user_service.get_all_arrangements_for_tourist(
            tourist_id=id
        )
        arrangements = GetArrangementSchema(many=True).dump(data)
        return arrangements


@users_api.route('/<int:id>/applications')
class ApplicationApi(Resource):
    # getting guides applications and status of application
    def get(self, id):
        data = user_service.get_all_applications_for_guide(
            travel_guide_id=id
        )
        return GetGuideArrangementSchema(many=True).dump(data)


@users_api.route('/login')
class UserLogin(Resource):
    # user login
    def post(self):
        post_data = user_login_schema.load(request.json)
        user = user_service.login_user(data=post_data)
        return GetUserSchema().dump(user)
