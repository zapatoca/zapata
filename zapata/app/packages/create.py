from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(
        __name__, template_folder="/app/templates", static_folder="/app/static"
    )
    return app


def create_db(app):
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://zapata:zapata@db:5432/zapata"
    return SQLAlchemy(app)
