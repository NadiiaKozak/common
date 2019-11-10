from flask import Flask

from Rooms import api_rooms
from Staff import api_staff
from Tenants import api_tenants
from config import run_config

app = Flask(__name__)

app.config.from_object(run_config())
app.register_blueprint(api_rooms)
app.register_blueprint(api_tenants)
app.register_blueprint(api_staff)



if __name__ == "__main__":
    app.run(debug=True)
