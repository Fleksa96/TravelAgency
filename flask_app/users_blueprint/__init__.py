from flask import Blueprint
from flask_restplus import Api

APP_NAME = 'users'
user_blueprint = Blueprint(APP_NAME,
                           __name__,
                           url_prefix='/{}'.format(APP_NAME))

users_api = Api(user_blueprint)

import flask_app.users_blueprint.api
