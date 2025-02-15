from flask import Blueprint
from .api import decoded_data
from .db import insert

routes = Blueprint('routes',__name__)

# header route
@routes.route("/", methods=["GET","POST"])
def insert_route():
    insert(decoded_data)
    return "Data commited to data"

@routes.route("/scheduler_test", methods=["GET","POST"])
def scheduler_test():
    return "Scheduler Test"
