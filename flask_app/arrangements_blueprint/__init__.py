from flask import Blueprint
from flask_restplus import Api

APP_NAME = 'arrangements'
arrangement_blueprint = Blueprint(APP_NAME,
                                  __name__,
                                  url_prefix='/{}'.format(APP_NAME))

arrangements_api = Api(arrangement_blueprint)

import flask_app.arrangements_blueprint.api
