from datetime import timedelta

from flask import Flask

from Rooms import api_rooms
from Staff import api_staff
from Tenants import api_tenants
from config import run_config
from create_db import create_db
from db import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app)
    app.permanent_session_lifetime = timedelta(minutes=20)  # add session expire time

    app.register_blueprint(create_db)
    app.register_blueprint(api_tenants)
    app.register_blueprint(api_rooms)
    app.register_blueprint(api_staff)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
