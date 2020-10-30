from flask_app import create_app
from config.development import Development as Conf

app = create_app(Conf)


@app.route("/")
def hello():
    return "HELLO WORLD!"
