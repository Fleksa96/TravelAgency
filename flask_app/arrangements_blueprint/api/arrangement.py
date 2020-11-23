from flask_restplus import Resource
from flask import request
from flask_login import login_required, current_user

from flask_app.arrangements_blueprint import arrangements_api
from flask_app.arrangements_blueprint.services \
    import ArrangementService
from flask_app.common_blueprint.schemas import \
    CreateArrangementSchema, GetArrangementSchema, UpdateArrangementSchema, \
    ArrangementMinimalSchema, GetApplicationSchema,\
    GetUserSchema, ArrangementSearchSchema, ReservationSchema
from flask_app.common_blueprint.services import GenericService

# schemas
create_arrangement_schema = CreateArrangementSchema()
get_arrangement_schema = GetArrangementSchema()
update_arrangement_schema = UpdateArrangementSchema()
arrangement_minimal_schema = ArrangementMinimalSchema(many=True)
get_user_schema = GetUserSchema(many=True)
get_search_schema = ArrangementSearchSchema()
reservation_schema = ReservationSchema()


# services
arrangement_service = ArrangementService()


@arrangements_api.route('')
class ArrangementApi(Resource):
    # getting all arrangements
    def get(self):
        data = arrangement_service.get_all_arrangements()
        arrangements = arrangement_minimal_schema.dump(data)
        return arrangements

    # posting new arrangement
    @login_required
    def post(self):
        post_data = create_arrangement_schema.load(request.json)
        arrangement = arrangement_service.create_arrangement(
            data=post_data
        )
        return get_arrangement_schema.dump(arrangement)


@arrangements_api.route('/search')
class ArrangementGuideApi(Resource):
    # getting all arrangements depending on query param travel guide
    @login_required
    def get(self):
        query_params = get_search_schema.load(request.args)
        data = arrangement_service.search_all_arrangements(
            query_params=query_params
        )
        arrangements = GetArrangementSchema(many=True).dump(data)
        return arrangements


@arrangements_api.route('/<int:id>')
class ArrangementIdApi(Resource):
    # returning arragnement by id
    @login_required
    def get(self, id):
        data = arrangement_service.get_arrangement_by_id(
            arrangement_id=id
        )
        arrangements = get_arrangement_schema.dump(data)
        return arrangements

    # deleting arrangement by id
    @login_required
    def delete(self, id):
        message = arrangement_service.delete_arrangement(
            arrangement_id=id
        )
        return message

    @login_required
    def patch(self, id):
        post_data = update_arrangement_schema.load(request.json)
        arrangement = arrangement_service.update_arrangement(
            data=post_data,
            id=id
        )
        return get_arrangement_schema.dump(arrangement)


@arrangements_api.route('/<int:id>/applications')
class ApplicationGuidesApi(Resource):
    # getting all travel guides with application
    # for arrangement_id
    @login_required
    def get(self, id):
        data = arrangement_service.get_all_guides_with_application(
            arrangement_id=id
        )
        travel_guides = get_user_schema.dump(data)
        return travel_guides

    @login_required
    def post(self, id):
        application = arrangement_service.create_application(
            travel_guide_id=current_user.id,
            arrangement_id=id
        )
        return GetApplicationSchema().dump(application)


@arrangements_api.route('/<int:id>/guides')
class ArrangementGuides(Resource):
    # getting all travel guides without arrangements and
    # travel guides with spare time
    @login_required
    def get(self, id):
        data = GenericService.get_all_available_travel_guides(
            arrangement_id=id
        )
        travel_guides = get_user_schema.dump(data)
        return travel_guides


@arrangements_api.route('/<int:id>/reservations')
class ArrangementReservationsApi(Resource):
    @login_required
    def post(self, id):
        data = reservation_schema.load(request.json)
        message = arrangement_service.create_reservation(
            arrangement_id=id,
            data=data,
            tourist_id=current_user.id
        )
        return message


@arrangements_api.route('/<int:arr_id>/reservations/<int:res_id>')
class ArrangementReservationsUpdateApi(Resource):
    @login_required
    def patch(self, arr_id, res_id):
        data = reservation_schema.load(request.json)
        message = arrangement_service.update_reservation(
            arrangement_id=arr_id,
            reservation_id=res_id,
            data=data,
            tourist_id=current_user.id
        )
        return message
