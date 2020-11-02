from flask_app import create_app
from config.development import Development as Conf

app = create_app(Conf)

if __name__ == '__main__':
    app.run(debug=True)
