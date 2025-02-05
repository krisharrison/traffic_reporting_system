from flask import Blueprint
import requests
import json


from .utils.constants import TOMTOM_API_VERSION, TOMTOM_API_KEY

tomtom_api = Blueprint('tomtom_api', __name__)

# api version and key imported from constants
api_version = TOMTOM_API_VERSION
api_key = TOMTOM_API_KEY


try:
    # Url & Payload strings
    url = "https://api.tomtom.com/traffic/services/{0}/incidentDetails".format(api_version)
    payload = {"key": api_key,
               "bbox": "-80.243527, 43.149550, -79.836727, 43.185858",
               "fields":"{incidents{type,geometry{type,coordinates},properties{id,iconCategory,magnitudeOfDelay,events{description,code,iconCategory},startTime,endTime,from,to,length,delay,roadNumbers,timeValidity,numberOfReports,lastReportTime,tmc{countryCode,tableNumber,tableVersion,direction,points{location,offset}}}}}",
               "categoryFilter": "0,1,2,3,4,5,6,7,8,9,10,11,14",
               "timeValidityFilter": "present"
               }

    api_response = requests.get(url, params=payload)
    api_response.raise_for_status()

except requests.HTTPError as err:
    print("Request could not be completed", err)


data = api_response.text
decoded_data = json.loads(data)
