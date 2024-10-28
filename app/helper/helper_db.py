
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
