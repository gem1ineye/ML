from collections import Counter

# -----------------------------------------
# Python: Counter Example
# -----------------------------------------
# Counter is a subclass of dict that counts hashable objects.
# It helps to track how many times each element appears in a list.

# -----------------------------------------
# Create a list with duplicate elements
# -----------------------------------------
L = ['Akash', 'manan', 'Akash', 'Manan', 'Vineet', 'Dev', 'Lalit']

# Create a Counter object (automatically counts occurrences)
c = Counter(L)

# Display the Counter dictionary
print(c)  # Example output: Counter({'Akash': 2, 'manan': 1, 'Manan': 1, 'Vineet': 1, 'Dev': 1, 'Lalit': 1})

# -----------------------------------------
# Access keys and values
# -----------------------------------------
print(c.keys())     # All unique elements
print(c.values())   # Their counts

# -----------------------------------------
# Update counts manually
# -----------------------------------------
# 'update()' adds new counts or increments existing ones
c.update({'Dev': 5})    # Adds +5 to 'Dev'
print(c)                # Now 'Dev' will have count 6 (1 + 5)

# -----------------------------------------
# Iterate through all elements
# -----------------------------------------
# 'elements()' returns each item repeated according to its count
for i in c.elements():
    print(i)

# -----------------------------------------
# Remove an item from Counter
# -----------------------------------------
c.pop('Akash')  # Deletes 'Akash' from the counter

# -----------------------------------------
# Find the most common elements
# -----------------------------------------
# Returns list of tuples (element, count) sorted by frequency
print(c.most_common(2))   # Top 2 most frequent elements
