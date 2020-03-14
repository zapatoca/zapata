#!/usr/bin/env python3


from modules.create import create_app, create_db
from modules.routes import configure_routes

app = create_app()
db = create_db(app)

configure_routes(app, db)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
