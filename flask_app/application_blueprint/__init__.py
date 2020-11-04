from flask import Blueprint
from flask_restplus import Api

APP_NAME = 'application'
applications_blueprint = Blueprint(APP_NAME,
                                  __name__,
                                  url_prefix='/{}'.format(APP_NAME))

application_api = Api(applications_blueprint)

import flask_app.application_blueprint.api
