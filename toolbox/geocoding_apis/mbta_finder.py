"""
Pinar Demetci 

Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
MBTA_BASE_URL = 'http://realtime.mbta.com/developer/api/v2/stopsbylocation'
MBTA_DEMO_API_KEY = 'wX9NwuHnZU2ToO7GmGR9uw'


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)
    response_json = json.loads(f.read())
    return response_json


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.

    >>> get_lat_long('Harvard University')
    (42.3770029, -71.11666009999999)
    """
    text_input = place_name.replace(' ', '')
    url=GMAPS_BASE_URL+'?address=?'+text_input
    response_data = get_json(url)
    latitude = response_data['results'][0]['geometry']['location']['lat']
    longitude = response_data['results'][0]['geometry']['location']['lng']
    return (latitude, longitude)

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    >>> get_nearest_station(*get_lat_long('Harvard University'))
    ('Harvard', 0.277270585298538)
    """
    url = MBTA_BASE_URL + '?api_key=' + MBTA_DEMO_API_KEY + '&lat=' + str(latitude) + '&lon=' + str(longitude)
    response= get_json(url)
    stations = []
    stations_d={}
    if response["stop"] == None:
        return "There are no stops close to your location"
    else:
        for x in response["stop"]:
            stations.append(x["parent_station_name"])
        for x, parent_station_name in enumerate(stations):
            if len(parent_station_name) != 0:
                stations_d[str(parent_station_name)]=float(str(response["stop"][x]["distance"]))
                stations_d_sorted=sorted(stations_d.items(), key=lambda item: item[1], reverse=False)
                return stations_d_sorted[0]

def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    >>> find_stop_near('Harvard University')
    (Nearest station, Distance): ('Harvard', 0.277270585298538)
    """
    location=get_lat_long(place_name)
    latitude=location[0]
    longitude=location[1]
    result= get_nearest_station(latitude,longitude)
    print '(Nearest station, Distance):', result

if __name__ == '__main__':
    import doctest
    doctest.testmod()