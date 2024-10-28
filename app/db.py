import mysql.connector
from mysql.connector import errorcode

import config


def insert():
    pass

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
    finally:
        conn.close()

