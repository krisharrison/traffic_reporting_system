import requests
import json
import constants

from flask import Flask


app = Flask(__name__)

api_version = constants.TOMTOM_API_VERSION
api_key = constants.TOMTOM_API_KEY

response_api = requests.get("https://api.tomtom.com/traffic/services/{0}/incidentDetails?key={1}&ids={ids}&fields={fields}&t={t}&categoryFilter={categoryFilter}&timeValidityFilter={timeValidityFilter}").format(0,1)



app.route("/incidents")
def hello_world():
    return response_api