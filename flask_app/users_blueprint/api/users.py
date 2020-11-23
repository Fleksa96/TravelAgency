from flask_restplus import Resource
from flask import request
from flask_login import login_user, logout_user, login_required, current_user

from flask_app.common_blueprint.schemas import \
    CreateUserSchema, GetUserSchema, UserLoginSchema, GetArrangementSchema,\
    GetGuideArrangementSchema, UpdateUserSchema, GetReservationSchema, \
    RegistrationUserSchema

from flask_app.users_blueprint import users_api
from flask_app.users_blueprint.services import \
    UserService

# schemas
create_user_schema = CreateUserSchema()
registration_user_schema = CreateUserSchema()
get_user_schema = GetUserSchema()
user_login_schema = UserLoginSchema()
update_user_schema = UpdateUserSchema()

# services
user_service = UserService()


@users_api.route('')
class UserRegistration(Resource):
    @login_required
    def post(self):
        post_data = create_user_schema.load(request.json)
        user = user_service.create_new_user(
            post_data=post_data,
            current_user=current_user
        )
        return GetUserSchema().dump(user)


@users_api.route('/me')
class UserData(Resource):
    # getting user data
    @login_required
    def get(self):
        user = user_service.get_user_by_id(
            user_id=current_user.id
        )
        return get_user_schema.dump(user)

    @login_required
    def patch(self):
        post_data = update_user_schema.load(request.json)
        user = user_service.update_user(
            user_id=current_user.id,
            data=post_data
        )
        return get_user_schema.dump(user)


@users_api.route('/registration')
class AdminCreateUserApi(Resource):
    # user registration
    def post(self):
        post_data = registration_user_schema.load(request.json)
        user = user_service.registration_of_new_user(post_data=post_data)
        return GetUserSchema().dump(user)


@users_api.route('/my-guides')
class GuideArrangementsApi(Resource):
    # getting all arangements for certain travel guide
    @login_required
    def get(self):
        data = user_service.get_all_arrangements_for_guide(
            travel_guide_id=current_user.id
        )
        arrangements = GetArrangementSchema(many=True).dump(data)
        return arrangements


@users_api.route('/reservations')
class ArrangementReservationApi(Resource):
    # getting tourist implementation arrangements
    @login_required
    def get(self):
        data = user_service.get_all_reservations_for_tourist(
            tourist_id=current_user.id
        )
        reservations = GetReservationSchema(many=True).dump(data)
        return reservations


@users_api.route('/applications')
class ApplicationApi(Resource):
    # getting guides applications and status of application
    @login_required
    def get(self):
        data = user_service.get_all_applications_for_guide(
            travel_guide_id=current_user.id
        )
        return GetGuideArrangementSchema(many=True).dump(data)


@users_api.route('/login')
class UserLogin(Resource):
    # user login
    def post(self):
        post_data = user_login_schema.load(request.json)
        user = user_service.login_user(data=post_data)
        login_user(user)
        return get_user_schema.dump(user)


@users_api.route('/logout')
class UserLogout(Resource):
    @login_required
    def get(self):
        logout_user()
        return {"message": 'You are logged out'}, 200
