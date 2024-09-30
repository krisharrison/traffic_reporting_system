import requests
import json
import constants

from flask import Flask


app = Flask(__name__)

api_version = constants.TOMTOM_API_VERSION
api_key = constants.TOMTOM_API_KEY

url = "https://api.tomtom.com/traffic/services/{0}/incidentDetails".format(api_version)
payload = {"key":api_key,"ids":"","fields":"{incidents{type,geometry{type,coordinates}}}","categoryFilter":"","timeValidityFilter":""}
api_response = requests.get(url,params=payload)

#Lat Min
4.165398
#Lat Max
4.165453

#Long min
80.243528
#Long Max




@app.route("/")
def get_api_response_header():
    return dict(api_response.headers)

@app.route("/data")
def get_api_response():
    return api_response.text

