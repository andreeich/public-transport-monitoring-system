import math

from modules.data_layer import DataConnector


# Business layer class that contains main logic of the program
class BusinessConnector(DataConnector):
    def __init__(self, test: bool = True) -> None:
        super().__init__(test)

        self._timetable = {}

        self._set_timetable()

    # Calculate estimated arrival time (in hours)
    def _calc_estimated_arrival_time(self, location: dict) -> float:
        lat = location['latitude']
        lon = location['longitude']
        # Find the transport vehicle closest to the given coordinates
        closest_vehicle = None
        closest_distance = float('inf')
        for vehicle in self._vehicles:
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
    def _set_timetable(self) -> None:
        for stop in self._stops:
            hour, minutes = divmod(
                self._calc_estimated_arrival_time(stop['location']), 1)
            self._timetable[stop['street']
                            ] = f"{int(hour)}h {int(round(minutes, 2) * 100)}m"

    # Calls functions for updating data
    def _update_data(self) -> None:
        super()._update_data()
        self._set_timetable()
