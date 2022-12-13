# Import the necessary modules
import requests
import json
import time
# Import the necessary modules from other files
from main import test

def get_locations():
    # Set the URL for the public transport location API
    api_url = 'https://example.com/api/transport/locations'
    # Set the location for the public transport locations data file
    file_url = 'locations.json'
    # Get current location of all the vehicles
    if (test):
        # Open local json file to get the current locations
        with open(file_url) as file:
            locations = json.load(file)
    else:
        # Make a GET request to the API to get the current locations
        response = requests.get(api_url)
        # Parse the response JSON
        locations = json.loads(response.text)
    return locations

def get_stops():
    # Set the URL for the public transport stops API
    api_url = 'https://example.com/api/transport/stops'
    # Set the location for the public transport stops data file
    file_url = 'stops.json'
    # Get current location of all the vehicles
    if (test):
        # Open local json file to get the current locations
        with open(file_url) as file:
            locations = json.load(file)
    else:
        # Make a GET request to the API to get the current locations
        response = requests.get(api_url)
        # Parse the response JSON
        locations = json.loads(response.text)
    return locations

def get_all_the_vehicles():
    # Print the locations
    print("List of all available vehicles:")
    for location in get_locations():
        print('Vehicle type:', location['type'])
        print('Vehicle number:', location['number'])
        print('Vehicle id:', location['vehicle_id'])
        print('Current location:', location['location']['latitude'], location['location']['longitude'])
        print()

def get_all_the_stops():
    # Print the stops
    print("List of all stops:")
    for location in get_stops():
        print('Street name:', location['street'])
        print('Is operating:', location['is_operating'])
        print('Location:', location['location']['latitude'], location['location']['longitude'])
        print()

def get_estimated_arrival_time(lat, lon):
  # Find the transport vehicle closest to the given coordinates
  closest_vehicle = None
  closest_distance = float('inf')
  for location in get_locations():
    # Calculate the distance between the given coordinates and the vehicle's current location
    distance = ((location['latitude'] - lat)**2 + (location['longitude'] - lon)**2)**0.5

    # If this distance is closer than the previous closest distance, update the closest vehicle and distance
    if distance < closest_distance:
      closest_vehicle = location['vehicle_id']
      closest_distance = distance

  # Calculate the estimated arrival time based on the vehicle's speed and the distance to the given coordinates
  estimated_arrival_time = closest_distance / closest_vehicle['speed']

  return estimated_arrival_time
