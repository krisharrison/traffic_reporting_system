from flask import Blueprint
from .api import decoded_data
from .db import insert

routes = Blueprint('routes',__name__)

# header route
@routes.route("/", methods=["POST"])
def insert_route():
    insert(decoded_data)
    return "Data displayed in terminal"
