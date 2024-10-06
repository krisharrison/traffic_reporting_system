import requests
import json
import constants

from flask import Flask


app = Flask(__name__)

api_version = constants.TOMTOM_API_VERSION
api_key = constants.TOMTOM_API_KEY

url = "https://api.tomtom.com/traffic/services/{0}/incidentDetails".format(api_version)
payload = {"key": api_key,
           "bbox": "-80.243527, 43.141332, -79.975639, 43.178831",
           "fields": "{incidents{type,geometry{type,coordinates}}}",
           "categoryFilter": "0,1,2,3,4,5,6,7,8,9,10,11,14",
           "timeValidityFilter": "present"
           }
api_response = requests.get(url, params=payload)


@app.route("/")
def get_api_response_header():
    return dict(api_response.headers)


@app.route("/data")
def get_api_response():
    return api_response.text
