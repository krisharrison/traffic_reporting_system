import requests
import json
import constants

from flask import Flask


app = Flask(__name__)

api_version = constants.TOMTOM_API_VERSION
api_key = constants.TOMTOM_API_KEY

response_api = requests.get("https://api.tomtom.com/traffic/services/{api_version}/incidentDetails?key={api_key}&ids={ids}&fields={fields}&t={t}&categoryFilter={categoryFilter}&timeValidityFilter={timeValidityFilter}")



app.route("/incidents")
def hello_world():
    return response_api