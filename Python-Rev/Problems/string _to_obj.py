import datetime

# -----------------------------------------
# Create a date object from user input
# -----------------------------------------

# Ask the user to enter a date in DD-MM-YYYY format
x = input('Enter date (DD-MM-YYYY): ')   # e.g., 21-10-2025

# Split the string by '-' to get day, month, and year as separate parts
d, m, y = x.split('-')   # Example: ['21', '10', '2025']

# Convert strings to integers and create a date object
date = datetime.date(int(y), int(m), int(d))

# Print the created date object
print(date)   # Output: 2025-10-21 (default ISO format: YYYY-MM-DD)
