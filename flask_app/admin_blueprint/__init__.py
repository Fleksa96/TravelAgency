from flask import Blueprint
from flask_restplus import Api

APP_NAME = 'admin_page'
administrator_blueprint = Blueprint(APP_NAME,
                                    __name__,
                                    url_prefix='/{}'.format(APP_NAME))

admin_api = Api(administrator_blueprint)

import flask_app.admin_blueprint.api
