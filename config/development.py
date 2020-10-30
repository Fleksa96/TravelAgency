from . import Config


class Development(Config):
    ENV_TYPE = "Development"

    DB_NAME = 'travel_agency'
    DB_USER = "agency_ceo"
    DB_PASSWORD = "agency_ceo"
    DB_HOST = "localhost"
    DB_PORT = 5432

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'. \
        format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'lovacportal.podrska@gmail.com'
    MAIL_PASSWORD = 'Aleksa-123'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
