from flask import Blueprint
from flask_restplus import Api

APP_NAME = 'homepage'
home_blueprint = Blueprint(APP_NAME,
                           __name__,
                           url_prefix='/{}'.format(APP_NAME))

homepage_api = Api(home_blueprint)

import flask_app.homepage_blueprint.api
