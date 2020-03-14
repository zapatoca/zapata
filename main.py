#!/usr/bin/env python3


import logging

from project.create import create_app, create_db
from project.routes import configure_routes

logging.basicConfig(filename='zapata.log', level=logging.DEBUG)

app = create_app()
db = create_db(app)

configure_routes(app, db)
