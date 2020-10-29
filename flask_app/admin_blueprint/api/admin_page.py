from flask_restplus import Resource
from flask import request

from flask_app.admin_blueprint import admin_api
from flask_app.admin_blueprint.services \
    import ArrangementService
from flask_app.admin_blueprint.schemas import \
    CreateArrangementSchema, GetArrangementSchema, DeleteArrangementSchema

# schemas
create_arrangement_schema = CreateArrangementSchema()
get_arrangement_schema = GetArrangementSchema()
delete_arrangement_schema = DeleteArrangementSchema()

# services
arrangement_service = ArrangementService()


@admin_api.route('/create_arrangement')
class CreateArrangement(Resource):
    def post(self):
        post_data = create_arrangement_schema.load(request.json)
        arrangement = arrangement_service.create_arrangement(data=post_data)
        return get_arrangement_schema.dump(arrangement)


@admin_api.route('/delete_arrangement')
class DeleteArrangement(Resource):
    def delete(self):
        post_data = delete_arrangement_schema.load(request.json)
        message = arrangement_service.delete_arrangement(data=post_data)
        return message
