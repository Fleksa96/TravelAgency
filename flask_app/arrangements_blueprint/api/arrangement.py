from flask_restplus import Resource
from flask import request
from flask_login import login_required

from flask_app.arrangements_blueprint import arrangements_api
from flask_app.arrangements_blueprint.services \
    import ArrangementService
from flask_app.common_blueprint.schemas import \
    CreateArrangementSchema, GetArrangementSchema

# schemas
create_arrangement_schema = CreateArrangementSchema()
get_arrangement_schema = GetArrangementSchema()

# services
arrangement_service = ArrangementService()


@arrangements_api.route('')
class ArrangementApi(Resource):
    def get(self):
        data = arrangement_service.get_all_arrangements()
        arrangements = GetArrangementSchema(many=True).dump(data)
        return arrangements

    # @login_required
    def post(self):
        post_data = create_arrangement_schema.load(request.json)
        arrangement = arrangement_service.create_arrangement(data=post_data)
        return get_arrangement_schema.dump(arrangement)


@arrangements_api.route('/<int:id>')
class DeleteArrangement(Resource):
    # @login_required
    def delete(self, id):
        message = arrangement_service.delete_arrangement(data=id)
        return message
