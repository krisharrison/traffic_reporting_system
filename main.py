from flask import Flask
from .app.db import traffic_db
from .app.api import tomtom_api
from .app.routes import routes

app = Flask(__name__)

app.register_blueprint(traffic_db)
app.register_blueprint(tomtom_api)
app.register_blueprint(routes)


