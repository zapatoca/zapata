#!/usr/bin/env python3


from zapata import create_app
from zapata.routes import configure_routes

app = create_app()

configure_routes(app)
