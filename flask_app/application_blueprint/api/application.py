from flask import request
from flask_restplus import Resource

from flask_app.application_blueprint import application_api
from flask_app.application_blueprint.services \
    import ApplicationService

from flask_app.common_blueprint.schemas \
    import GetGuideArrangementSchema, \
    GetApplicationSchema, CreateApplicationSchema

# services
application_service = ApplicationService()

# schemas
get_guide_arrangement_schema = GetGuideArrangementSchema(many=True)
create_application_schema = CreateApplicationSchema()


@application_api.route('/<int:id>')
class ApplicationApi(Resource):
    # getting guides applications and status of application
    def get(self, id):
        data = application_service.get_all_arrangements_for_travel_guide(
            travel_guide_id=id
        )
        return get_guide_arrangement_schema.dump(data)

    # posting application from travel_guide
    def post(self, id):
        post_data = create_application_schema.load(request.json)
        application = application_service.create_application(
            travel_guide_id=id,
            post_data=post_data
        )
        return GetApplicationSchema().dump(application)
