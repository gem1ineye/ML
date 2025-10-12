import datetime as dt

class EventPlanner:
    def __init__(self, year):
        # Initialize planner for a specific year
        self.year = year
        self.events = {}   # Dictionary to store events {date: details}

    def add(self, when, details):
        """
        ✅ Add a new event.
        - Accepts either a 'datetime.date' object or a date string in 'dd/mm/YYYY' format.
        - Validates that the date is not in the past and belongs to the same planner year.
        """
        
        # Convert string date to datetime.date if needed
        if isinstance(when, str):
            when = dt.datetime.strptime(when, '%d/%m/%Y').date()
        
        # Validate date (must be in current planner year and not in the past)
        if when < dt.date.today() or when.year != self.year:
            raise Exception('Invalid Date! Must be in the current planner year and not in the past.')
        
        # Store the event
        self.events[when] = details

    def remove_event(self, when):
        """
        ✅ Remove an event for a given date (string or datetime.date)
        """
        if isinstance(when, str):
            when = dt.datetime.strptime(when, '%d/%m/%Y').date()
        
        # Check if event exists
        if when in self.events:
            del self.events[when]
            print(f"Event on {when.strftime('%d/%m/%Y')} removed successfully!")
        else:
            print("⚠️ Event not found!")

    def list_events(self):
        """
        ✅ Display all stored events in sorted order by date.
        """
        print(f"\n📅 Events for {self.year}:")
        if not self.events:
            print("No events added yet.")
        else:
            for date_obj, details in sorted(self.events.items()):
                # Format the date nicely (e.g., 27 May 2025 (Tuesday))
                print(date_obj.strftime('%d %B %Y (%A)'))
                print('  Details:', details)
                print('-' * 30)


# --- Main Program ---

year = int(input('Enter Year: '))
planner = EventPlanner(year)

# Adding events
planner.add('27/05/2025', "Having Party with friends")
planner.add('12/06/2025', "Team outing")

# Displaying all events
planner.list_events()
