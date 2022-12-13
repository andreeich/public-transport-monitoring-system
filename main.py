# Import the necessary modules
import requests
import json
import time
# Import the necessary modules from other files
from functions import *

# Set testing variable for using location data from an API or local file
test = True

# Set the frequency for checking the locations (in seconds)
update_frequency = 60

# Main part of the program
while True:
    get_all_the_vehicles()
    get_all_the_stops()

    # Sleep for the specified number of seconds before checking again
    time.sleep(update_frequency)
