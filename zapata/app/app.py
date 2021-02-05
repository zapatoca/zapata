#!/usr/bin/env python3

from flask import Flask

from database import db
from models import *  # noqa
from router import router

app = Flask(
    __name__, template_folder="/app/templates", static_folder="/app/static"
)
app.secret_key = "secret123"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://zapata:zapata@db:5432/zapata"
db.init_app(app)

app.register_blueprint(router)


def main() -> None:
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True, host="0.0.0.0")


if __name__ == "__main__":
    main()  # pragma: no cover
