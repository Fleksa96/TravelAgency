from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

from flask_app.users_blueprint import user_blueprint
from flask_app.arrangements_blueprint import arrangement_blueprint
from flask_app.application_blueprint import applications_blueprint


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(user_blueprint)
    app.register_blueprint(arrangement_blueprint)
    app.register_blueprint(applications_blueprint)

    return app


from data_layer.models import Arrangement, User
