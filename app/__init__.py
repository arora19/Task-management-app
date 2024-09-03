from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager

# initialize the extensions (without binding to the app yet)
db = SQLAlchemy()
jwt = JWTManager()


def create_app():
    # create the flask app instance
    app = Flask(__name__)

    # configure the app(add your configs here)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # using sqlite for simplicity
    app.config['SECRET_KEY'] = 'your_secret_key'  # replace with strong secret key
    app.config['JWT_SECRET_KEY'] = 'your_swt_secret_key'  # replace with a strong JWT secret key

    # initialize the extensions with the app
    db.init_app(app)
    jwt.init_app(app)

    # import and initialize routes
    from .routes import initialize_routes
    api = Api(app)
    initialize_routes(api)

    return app

