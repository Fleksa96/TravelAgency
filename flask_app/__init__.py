from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from werkzeug.utils import redirect

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
login_manager = LoginManager()

from flask_app.users_blueprint import user_blueprint
from flask_app.arrangements_blueprint import arrangement_blueprint


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    app.register_blueprint(user_blueprint)
    app.register_blueprint(arrangement_blueprint)

    return app


from data_layer import Arrangement, User, Reservation, Application


@login_manager.user_loader
def load_user(user_id):
    if user_id is None:
        return redirect('/')

    user = User.query.filter(User.id == int(user_id)).first()
    return user
