import datetime as dt

# -----------------------------------------
# Function to find the previous occurrence of a given weekday
# -----------------------------------------
def prev_day(day):
    # List of weekdays (Python's weekday() gives 0 for Monday, 6 for Sunday)
    week_day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    # Get today's date
    today = dt.date.today()
    
    # Get today's weekday index (0 = Monday, 6 = Sunday)
    t_dw = today.weekday()
    
    # Get the index of the target day (e.g., 'monday' → 0)
    dw = week_day.index(day.lower())
    
    # Calculate difference in days
    diff = dw - t_dw
    
    # If diff < 0 → target day already passed this week
    # Else → we need to go back to last week's occurrence of that day
    if diff < 0:
        new_date = today + dt.timedelta(diff)
    else:
        new_date = today + dt.timedelta(-(7 - diff))
    
    return new_date


# -----------------------------------------
# Example Usage
# -----------------------------------------
print('Today :', dt.date.today())          # Prints today's date
print('Prev Monday :', prev_day('monday')) # Prints date of last Monday
