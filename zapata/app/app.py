#!/usr/bin/env python3

from flask import Flask

import models.fee  # noqa
from database import db
from models_ import *  # noqa
from router import router
from routers.fees import fees_router
from routers.index import index_router

app = Flask(__name__, template_folder="/templates", static_folder="/static")
app.secret_key = "secret123"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://zapata:zapata@db:5432/zapata"
db.init_app(app)

app.register_blueprint(router)
app.register_blueprint(index_router)
app.register_blueprint(fees_router)


def main() -> None:
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True, host="0.0.0.0", port=3000)


if __name__ == "__main__":
    main()  # pragma: no cover
