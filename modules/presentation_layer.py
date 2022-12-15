import asyncio

from modules.business_layer import BusinessConnector


# Presentation layer class that contains methods for
# outputting data and main loop menu with async update method
# for providing up-to-date data
class PresentationConnector(BusinessConnector):
    def __init__(self, test: bool = True, autostart: bool = True) -> None:
        super().__init__(test)

        self._update_frequency = 60 # Delay for updating data function (in seconds)

        if autostart: self.start() # Run main loop 

    # Print list of all available vehicles
    def _print_vehicles(self) -> None:
        print("List of all available vehicles:")
        for vehicle in self._vehicles:
            print('Vehicle type:', vehicle['type'])
            print('Vehicle number:', vehicle['number'])
            print('Vehicle id:', vehicle['vehicle_id'])
            print('Current location:',
                vehicle['location']['latitude'], vehicle['location']['longitude'])
            print()

    # Print list of all stops
    def _print_stops(self) -> None:
        print("List of all stops:")
        for stop in self._stops:
            print('Street name:', stop['street'])
            print('Is operating:', stop['is_operating'])
            print('Location:', stop['location']
                ['latitude'], stop['location']['longitude'])
            print()

    # Print timetable (Name of the street | Nearest vehicle arriving time)
    def _print_timetable(self) -> None:
        print("Timetable:")
        for street, time_left in self._timetable.items():
            print("Street:", street)
            print('Time left:', time_left)
            print()

    # Print time left value for user's choice street
    def _print_time_from_timetable(self) -> None:
        counter = 1
        # Print the menu options
        for stop in self._timetable:
            print(f"{counter}. {stop}")
            counter += 1
        # Prompt the user for their choice
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            # If the user's choice is valid, call the corresponding
            # function from the options dictionary
            if choice >= 1 and choice < counter:
                print("Arriving time:", list(self._timetable.values())[choice-1])
                print()
            else:
                print("Invalid choice. Please try again.")
                print()
        except ValueError as e:
            print("ERROR:", e)

    # Async version of update_data
    async def _update_data(self) -> None:
        while True:
            # print('Data was updated')
            super()._update_data()
            await asyncio.sleep(self._update_frequency)

    # Main loop function
    async def _menu(self):
        # Ensure that the event loop is running
        loop = asyncio.get_running_loop()

        # Schedule the periodic task
        task = loop.create_task(self._update_data())

        # Define a dictionary that maps the user's choice
        # to the corresponding code to run
        options = {
            "1": self._print_timetable,
            "2": self._print_time_from_timetable,
            "3": quit
        }

        # Keep displaying the menu and accepting input until
        # the user selects the option to quit
        while True:
            await asyncio.sleep(0)
            print("Menu:")
            # Print the menu options
            print("1. Get full timetable")
            print("2. Get arr. time for street")
            print("3. Quit")

            # Prompt the user for their choice
            choice = input("Enter your choice: ")

            # If the user's choice is valid, call the corresponding
            # function from the options dictionary
            if choice in options:
                options[choice]()
            # If the user's choice is not valid, display an error message
            else:
                print("Invalid choice. Please try again.")
        await task

    # Start menu loop
    def start(self):
        asyncio.run(self._menu())
        
