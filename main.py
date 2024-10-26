import requests
import json
import mysql.connector
from mysql.connector import errorcode

import constants
import config

from flask import Flask


app = Flask(__name__)

# api version and key imported from constants
api_version = constants.TOMTOM_API_VERSION
api_key = constants.TOMTOM_API_KEY

# Url & Payload strings
url = "https://api.tomtom.com/traffic/services/{0}/incidentDetails".format(api_version)
payload = {"key": api_key,
           "bbox": "-80.243527, 43.149550, -79.836727, 43.185858",
           "fields":"{incidents{type,geometry{type,coordinates},properties{id,iconCategory,magnitudeOfDelay,events{description,code,iconCategory},startTime,endTime,from,to,length,delay,roadNumbers,timeValidity,numberOfReports,lastReportTime,tmc{countryCode,tableNumber,tableVersion,direction,points{location,offset}}}}}",
           "categoryFilter": "0,1,2,3,4,5,6,7,8,9,10,11,14",
           "timeValidityFilter": "present"
           }

# Tomtom response object
api_response = requests.get(url, params=payload)

# writing to the database
try:
    conn = mysql.connector.connect(user=config.username, password=config.database_key, host='127.0.0.1', database='traffic_db')
    with conn.cursor() as cursor:
        add_incident = ("INSERT INTO incidents"
                         "(id, iconCategory, magnitudeOfDelay, startTime, eventDescription) "
                         "VALUES(%(id)s, %(iconCategory)s, %(magintudeOfDelay)s, %(startTime)s, %(evenDescription)s")

        add_coordindates = ("INSERT INTO coordinates"
                            "(coordinates_id, incidents_id, latitude, longitude)"
                            "VALUES(%(coordinates_id)s, %(incidents_id)s, %(latitude)s, %(longitude)s)")

        # cursor.execute()
        # conn.commit()

        print("Record comitted successfully")

except mysql.connector.Error as err:
    if err.errno == errorcode.EA_ACCESS_DENIED_ACCESS:
        print("Something wrong with the username and password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)



# get incident from json obj
# return incident dict
def get_incident(incident):
    # Incidents table data
    id = incident["id"]
    iconCategory = incident["iconCategory"]
    magnitudeOfDelay = incident["magnitudeOfDelay"]
    startTime = incident["startTime"]
    description = incident["events"][0]["description"]

    # incidents table data
    incidents_data = {
        "id": id,
        "iconCategory": iconCategory,
        "magnitudeOfDelay": magnitudeOfDelay,
        "startTime": startTime,
        "description": description
    }

    return incidents_data



# get coordinates from json obj
# return coordinates dict
def get_coordinates(coordinates, incident_id):
    # Coordinates table data
    incidents_id = incident_id
    latitude = coordinates[1]
    longitude = coordinates[0]

    # Coordinates table data
    coordinates_data = {
        "incidents_id": incidents_id,
        "latitude": latitude,
        "longitude": longitude
    }
    return coordinates_data


data = api_response.text
decoded_data = json.loads(data)
incidents_length = len(decoded_data["incidents"]) - 1



# Grab data from JSON response
# Outer loop is for data to be comitted to the incidents table
# Inner loop is for data to be commited to the coordinates table
for incident_index in range(incidents_length):
    print(end="\n")
    # set incident
    # get incident data
    # insert incident data
    incident = decoded_data["incidents"][incident_index]["properties"]
    incident_data = get_incident(incident)
    print(incident_data)

    # Coordinates length at index *incident_index*
    coordinates_length = len(decoded_data["incidents"][incident_index]["geometry"]["coordinates"]) - 1
    for coordinates_index in range(coordinates_length):
         
        coordinates = decoded_data["incidents"][incident_index]["geometry"]["coordinates"][coordinates_index]
        incident_id = incident_data["id"]
        coordinates_data = get_coordinates(coordinates,incident_id)
        print(coordinates_data)
        



# header route
@app.route("/")
def get_api_response_header():
    return dict(api_response.headers)


# payload route
@app.route("/data")
def get_api_response():
    data = api_response.text
    decoded_data = json.loads(data)
    return decoded_data
