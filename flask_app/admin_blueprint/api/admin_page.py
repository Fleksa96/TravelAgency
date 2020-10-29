from flask_restplus import Resource
from flask import request

from flask_app.admin_blueprint import admin_api
from flask_app.admin_blueprint.services \
    import ArrangementService
from flask_app.admin_blueprint.schemas import \
    CreateArrangementSchema, GetArrangementSchema

#schemas
create_arrangement_schema = CreateArrangementSchema()
get_arrangement_schema = GetArrangementSchema()

#services
arrangement_service = ArrangementService()


@admin_api.route('/insert_arrangement')
class CreateArrangement(Resource):
    def post(self):
        post_data = create_arrangement_schema.load(request.json)
        arrangement = arrangement_service.create_arrangement(post_data)
        return get_arrangement_schema.dump(arrangement)
