# Import the necessary modules
import requests
import json
import math

# Set testing variable for using location data from an API or local file
test = True

# Set timetable for collecting data (Name of the street | Nearest vehicle arriving time)
timetable = {}

# Get parsed json data dictionary about vehicles


def get_vehicles():
    # Set the URL for the public transport vehicles API
    api_url = 'https://example.com/api/transport/locations'
    # Set the vehicles for the public transport vehicles data file
    file_url = 'vehicles.json'
    # Get current vehicles of all the vehicles
    if (test):
        # Open local json file to get the current vehicles
        with open(file_url) as file:
            vehicles = json.load(file)
    else:
        # Make a GET request to the API to get the current vehicles
        response = requests.get(api_url)
        # Parse the response JSON
        vehicles = json.loads(response.text)
    return vehicles

# Get parsed json data dictionary about stops


def get_stops():
    # Set the URL for the public transport stops API
    api_url = 'https://example.com/api/transport/stops'
    # Set the location for the public transport stops data file
    file_url = 'stops.json'
    # Get current location of all the vehicles
    if (test):
        # Open local json file to get the current stops
        with open(file_url) as file:
            stops = json.load(file)
    else:
        # Make a GET request to the API to get the current stops
        response = requests.get(api_url)
        # Parse the response JSON
        stops = json.loads(response.text)
    return stops

# Print list of all available vehicles


def print_vehicles():
    # Print the vehicles
    print("List of all available vehicles:")
    for vehicle in get_vehicles():
        print('Vehicle type:', vehicle['type'])
        print('Vehicle number:', vehicle['number'])
        print('Vehicle id:', vehicle['vehicle_id'])
        print('Current location:',
              vehicle['location']['latitude'], vehicle['location']['longitude'])
        print()

# Print list of all stops


def print_stops():
    # Print the stops
    print("List of all stops:")
    for stop in get_stops():
        print('Street name:', stop['street'])
        print('Is operating:', stop['is_operating'])
        print('Location:', stop['location']
              ['latitude'], stop['location']['longitude'])
        print()

# Calculate estimated arrival time (in hours)


def get_estimated_arrival_time(location):
    lat = location['latitude']
    lon = location['longitude']
    # Find the transport vehicle closest to the given coordinates
    closest_vehicle = None
    closest_distance = float('inf')
    for vehicle in get_vehicles():
        # Calculate the distance (km) between the given coordinates and the vehicle's current location
        R = 6371  # radius of earth in kilometers
        phi1 = math.radians(lat)
        phi2 = math.radians(vehicle['location']['latitude'])
        delta_phi = math.radians(vehicle['location']['latitude'] - lat)
        delta_lambda = math.radians(vehicle['location']['longitude'] - lon)

        a = math.sin(delta_phi / 2)**2 + math.cos(phi1) * \
            math.cos(phi2) * math.sin(delta_lambda / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c

        # If this distance is closer than the previous closest distance, update the closest vehicle and distance
        if distance < closest_distance:
            closest_vehicle = vehicle
            closest_distance = distance

    # Calculate the estimated arrival time (hour) based on the vehicle's speed (km/hour) and the distance to the given coordinates
    estimated_arrival_time = closest_distance / closest_vehicle['speed']

    return estimated_arrival_time

# Calculate and collect timetable data into dictionary


def get_timetable():
    for stop in get_stops():
        hour, minutes = divmod(get_estimated_arrival_time(stop['location']), 1)
        timetable[stop['street']
                  ] = f"{int(hour)}h {int(round(minutes, 2) * 100)}m"

# Print timetable (Name of the street | Nearest vehicle arriving time)


def print_timetable():
    get_timetable()
    print("Timetable:")
    for street, time_left in timetable.items():
        print("Street:", street)
        print('Time left:', time_left)
        print()


def get_time_from_timetable():
    get_timetable()
    counter = 1
    # Print the menu options
    for stop in timetable:
        print(f"{counter}. {stop}")
        counter += 1
    # Prompt the user for their choice
    choice = input("Enter your choice: ")
    try:
        choice = int(choice)
        # If the user's choice is valid, call the corresponding
        # function from the options dictionary
        if choice >= 1 and choice < counter:
            print("Arriving time:", list(timetable.values())[choice-1])
            print()
    except ValueError as e:
        print("ERROR:", e)


def main():
    # Define a dictionary that maps the user's choice
    # to the corresponding code to run
    options = {
        "1": print_stops,
        "2": print_timetable,
        "3": get_time_from_timetable,
        "4": quit
    }

    # Keep displaying the menu and accepting input until
    # the user selects the option to quit
    while True:
        # Print the menu options
        print("1. Show all the stops")
        print("2. Get full timetable")
        print("3. Get arr. time for chosen street")
        print("4. Quit")

        # Prompt the user for their choice
        choice = input("Enter your choice: ")

        # If the user's choice is valid, call the corresponding
        # function from the options dictionary
        if choice in options:
            options[choice]()

        # If the user's choice is not valid, display an error message
        else:
            print("Invalid choice. Please try again.")
