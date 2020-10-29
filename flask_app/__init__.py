from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from flask_app.homepage_blueprint import home_blueprint
from flask_app.admin_blueprint import administrator_blueprint


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_blueprint)
    app.register_blueprint(administrator_blueprint)

    return app


from data_layer.models import Arrangement, User
