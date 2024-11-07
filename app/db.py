from flask import Blueprint
import mysql.connector
from mysql.connector import errorcode

from .utils.config import database_key, username
from .helper.helper_db import get_incident, get_coordinates

traffic_db = Blueprint('traffic_db',__name__)

def insert(decoded_data):

    # writing to the database
    try:
        conn = mysql.connector.connect(user=username, password=database_key, host='127.0.0.1', database='traffic_db')
        with conn.cursor() as cursor:
            add_incident = ("INSERT INTO incidents"
                           "(id, iconCategory, magnitudeOfDelay, startTime, eventDescription) "
                           "VALUES(%(id)s, %(iconCategory)s, %(magnitudeOfDelay)s, %(startTime)s, %(eventDescription)s")

            add_coordindates = ("INSERT INTO coordinates"
                               "(coordinates_id, incidents_id, latitude, longitude) "
                               "VALUES(%(coordinates_id)s, %(incidents_id)s, %(latitude)s, %(longitude)s)")


            
            incidents_length = len(decoded_data["incidents"]) - 1
            # Grab data from JSON response
            # Outer loop is for data to be comitted to the incidents table
            # Inner loop is for data to be commited to the coordinates table
            for incident_index in range(incidents_length):
                # set incident
                # get incident data
                # insert incident data
                incident = decoded_data["incidents"][incident_index]["properties"]
                incident_data = get_incident(incident)
                cursor.execute(add_incident, incident_data)

                # Coordinates length at index *incident_index*
                coordinates_length = len(decoded_data["incidents"][incident_index]["geometry"]["coordinates"]) - 1
                for coordinates_index in range(coordinates_length):
         
                    coordinates = decoded_data["incidents"][incident_index]["geometry"]["coordinates"][coordinates_index]
                    incident_id = incident_data["id"]
                    coordinates_data = get_coordinates(coordinates,incident_id)
                    cursor.execute(add_coordindates, coordinates_data)
        
                conn.commit()
                print("Record comitted successfully")


    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something wrong with the username and password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        conn.close()

