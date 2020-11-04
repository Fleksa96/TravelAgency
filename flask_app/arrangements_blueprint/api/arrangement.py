from flask_restplus import Resource
from flask import request
from flask_login import login_required

from flask_app.arrangements_blueprint import arrangements_api
from flask_app.arrangements_blueprint.services \
    import ArrangementService
from flask_app.common_blueprint.schemas import \
    CreateArrangementSchema, GetArrangementSchema, UpdateArrangementSchema, \
    ArrangementMinimalSchema

# schemas
create_arrangement_schema = CreateArrangementSchema()
get_arrangement_schema = GetArrangementSchema()
update_arrangement_schema = UpdateArrangementSchema()
arrangement_minimal_schema = ArrangementMinimalSchema(many=True)

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


@arrangements_api.route('/no-travel-guide')
class ArrangementNoGuideApi(Resource):
    # getting all arrangements without travel guide
    def get(self):
        data = arrangement_service.get_all_arrangements_without_guide()
        arrangements = GetArrangementSchema(many=True).dump(data)
        return arrangements


@arrangements_api.route('/travel-guide/<int:id>')
class ArrangementGuideApi(Resource):
    # getting all arangements for certain travel guide
    def get(self, id):
        data = arrangement_service.get_all_arrangements_for_guide(
            travel_guide_id=id
        )
        arrangements = GetArrangementSchema(many=True).dump(data)
        return arrangements


@arrangements_api.route('/reservation/<int:id>')
class ArrangementReservationApi(Resource):
    # getting tourist reservation arrangements
    def get(self, id):
        data = arrangement_service.get_all_arrangements_for_tourist(
            tourist_id=id
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
    # updating arrangement, need to add validation
    def patch(self, id):
        post_data = update_arrangement_schema.load(request.json)
        arrangement = arrangement_service.update_arrangement(
            data=post_data,
            id=id
        )
        return get_arrangement_schema.dump(arrangement)
