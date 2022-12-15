import requests
import json


# Data layer class that providing up-to-date data taking
# it from an API or a local files 
class DataConnector:
    def __init__(self, test: bool = True) -> None:
        self.test = test
        self._vehicles   = []
        self._stops      = []

        self._load_vehicles()
        self._load_stops()

    # Get parsed json data dictionary about vehicles
    def _load_vehicles(self) -> None:
        # Set the URL for the public transport vehicles API
        api_url = 'https://example.com/api/transport/locations'
        # Set the vehicles for the public transport vehicles data file
        file_url = 'vehicles.json'
        # Get current vehicles of all the vehicles
        if (self.test):
            # Open local json file to get the current vehicles
            with open(file_url) as file:
                vehicles = json.load(file)
        else:
            # Make a GET request to the API to get the current vehicles
            response = requests.get(api_url)
            # Parse the response JSON
            vehicles = json.loads(response.text)
        self._vehicles = vehicles

    # Get parsed json data dictionary about stops
    def _load_stops(self) -> None:
        # Set the URL for the public transport stops API
        api_url = 'https://example.com/api/transport/stops'
        # Set the location for the public transport stops data file
        file_url = 'stops.json'
        # Get current location of all the vehicles
        if (self.test):
            # Open local json file to get the current stops
            with open(file_url) as file:
                stops = json.load(file)
        else:
            # Make a GET request to the API to get the current stops
            response = requests.get(api_url)
            # Parse the response JSON
            stops = json.loads(response.text)
        self._stops = stops

    # Calls functions for updating data
    def _update_data(self) -> None:
        self._load_vehicles()
        self._load_stops()