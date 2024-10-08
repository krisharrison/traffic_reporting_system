import requests
import constants
import mysql.connector
import config

from flask import Flask


app = Flask(__name__)

# api version and key imported from constants
api_version = constants.TOMTOM_API_VERSION
api_key = constants.TOMTOM_API_KEY

# Url & Payload strings
url = "https://api.tomtom.com/traffic/services/{0}/incidentDetails".format(api_version)
payload = {"key": api_key,
           "bbox": "-80.243527, 43.141332, -79.975639, 43.178831",
           "fields":"{incidents{type,geometry{type,coordinates},properties{id,iconCategory,magnitudeOfDelay,events{description,code,iconCategory},startTime,endTime,from,to,length,delay,roadNumbers,timeValidity,numberOfReports,lastReportTime,tmc{countryCode,tableNumber,tableVersion,direction,points{location,offset}}}}}",
           "categoryFilter": "0,1,2,3,4,5,6,7,8,9,10,11,14",
           "timeValidityFilter": "present"
           }

# Tomtom response object
api_response = requests.get(url, params=payload)

# Connecting to database
conn = mysql.connector.connect(user=config.username, password=config.database_key, host='127.0.0.1', database='traffic_db')


# header route
@app.route("/")
def get_api_response_header():
    return dict(api_response.headers)


# payload route
@app.route("/data")
def get_api_response():
    return api_response.json()
