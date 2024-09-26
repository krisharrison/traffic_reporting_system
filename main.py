import requests
import json
import constants

from flask import Flask


app = Flask(__name__)

api_version = constants.TOMTOM_API_VERSION
api_key = constants.TOMTOM_API_KEY

url = "https://api.tomtom.com/traffic/services/{0}/incidentDetails".format(api_version)
payload = {"key":api_key,"ids":"","fields":"{incidents{type,geometry{type,coordinates}}}","categoryFilter":"","timeValidityFilter":""}#,"t":"1727310440"
api_response = requests.get(url,params=payload)



@app.route("/")
def get_api_response_header():
    return dict(api_response.headers)

@app.route("/data")
def get_api_response():
    return api_response.json()

