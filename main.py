# Import the necessary modules
import requests
import json
import time

# Set testing variable for using location data from an API or local file
test = True

# Set the frequency for checking the locations (in seconds)
update_frequency = 60

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

# Main part of the program
while True:
    get_all_the_vehicles()

    # Sleep for the specified number of seconds before checking again
    time.sleep(update_frequency)
