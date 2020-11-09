from flask_restplus import Resource
from flask import request
from flask_login import login_required

from flask_app.arrangements_blueprint import arrangements_api
from flask_app.arrangements_blueprint.services \
    import ArrangementService
from flask_app.common_blueprint.schemas import \
    CreateArrangementSchema, GetArrangementSchema, UpdateArrangementSchema, \
    ArrangementMinimalSchema, CreateApplicationSchema, GetApplicationSchema,\
    GetUserSchema
from flask_app.common_blueprint.services import GenericService

# schemas
create_arrangement_schema = CreateArrangementSchema()
get_arrangement_schema = GetArrangementSchema()
update_arrangement_schema = UpdateArrangementSchema()
arrangement_minimal_schema = ArrangementMinimalSchema(many=True)
create_application_schema = CreateApplicationSchema()
get_user_schema = GetUserSchema(many=True)


# services
arrangement_service = ArrangementService()


@arrangements_api.route('')
class ArrangementApi(Resource):
    # getting all arrangements
    def get(self):
        data = arrangement_service.get_all_arrangements()
        arrangements = arrangement_minimal_schema.dump(data)
        return arrangements

    # @login_required
    # posting new arrangement
    def post(self):
        post_data = create_arrangement_schema.load(request.json)
        arrangement = arrangement_service.create_arrangement(
            data=post_data
        )
        return get_arrangement_schema.dump(arrangement)


@arrangements_api.route('/search')
class ArrangementGuideApi(Resource):
    # getting all arrangements depending on query param travel guide
    def get(self):
        has_travel_guide = request.args.get('has-travel-guide')
        if not has_travel_guide:
            has_travel_guide = False
        data = arrangement_service.get_all_arrangements_depending_guide(
            has_travel_guide=has_travel_guide
        )
        arrangements = GetArrangementSchema(many=True).dump(data)
        return arrangements


@arrangements_api.route('/<int:id>')
class ArrangementIdApi(Resource):
    # returning arragnement by id
    def get(self, id):
        data = arrangement_service.get_arrangement_by_id(
            arrangement_id=id
        )
        arrangements = get_arrangement_schema.dump(data)
        return arrangements

    # @login_required
    # deleting arrangement by id
    def delete(self, id):
        message = arrangement_service.delete_arrangement(
            arrangement_id=id
        )
        return message

    # @login_required
    def patch(self, id):
        post_data = update_arrangement_schema.load(request.json)
        arrangement = arrangement_service.update_arrangement(
            data=post_data,
            id=id
        )
        return get_arrangement_schema.dump(arrangement)


# this post method will be move to ApplicationGuidesApi once current user
# is implemented
@arrangements_api.route('/<int:id>/applications/<int:guide_id>')
class ArrangementApplicationApi(Resource):
    # posting application from travel_guide
    def post(self, id, guide_id):
        application = arrangement_service.create_application(
            travel_guide_id=guide_id,
            arrangement_id=id
        )
        return GetApplicationSchema().dump(application)


@arrangements_api.route('/<int:id>/applications')
class ApplicationGuidesApi(Resource):
    # getting all travel guides with application
    # for arrangement_id
    def get(self, id):
        data = arrangement_service.get_all_guides_with_application(
            arrangement_id=id
        )
        travel_guides = get_user_schema.dump(data)
        return travel_guides


@arrangements_api.route('/<int:id>/guides')
class ArrangementGuides(Resource):
    # getting all travel guides without arrangements and
    # travel guides with spare time
    def get(self, id):
        data = GenericService.get_all_travel_guides_without_arrangement(
            arrangement_id=id
        )
        travel_guides = get_user_schema.dump(data)
        return travel_guides
