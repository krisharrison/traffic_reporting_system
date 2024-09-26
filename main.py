import requests
import json
import constants

from flask import Flask


app = Flask(__name__)

api_version = constants.TOMTOM_API_VERSION
api_key = constants.TOMTOM_API_KEY

url = "https://api.tomtom.com/traffic/services/{0}/incidentDetails".format(api_version)
payload = {"key":api_key,"ids":"","fields":"{incidents{type,geometry{type,coordinates}}}","t":"1727310440","categoryFilter":"","timeValidityFilter":""}
api_response = requests.get(url,params=payload)



@app.route("/")
def get_api_response():
    return api_response.text



