import bisect as b    # 'bisect' module helps maintain sorted lists efficiently

class Sorted_lst:
    
    def __init__(self):
        # Initialize an empty list
        self.lst = []
        
    def add(self, val):
        """
        ✅ Adds a new value while keeping the list sorted.
        'insort' inserts the element in its correct position automatically.
        """
        b.insort(self.lst, val)
    
    def remove(self, value):
        """
        ✅ Removes a specific value from the list.
        (Raises ValueError if the value is not found)
        """
        self.lst.remove(value)
    
    def search(self, key):
        """
        ✅ Returns the index position of the given key in the sorted list.
        (Linear search — could be optimized using bisect for faster lookup)
        """
        return self.lst.index(key)
    
    def insert_pos(self, val):
        """
        ✅ Finds the position where a new value should be inserted to maintain order.
        'bisect_left' returns the index where val can be inserted (before any equal elements).
        """
        position = b.bisect_left(self.lst, val)
        return position
    
    def display(self):
        """Displays the current list."""
        print(self.lst)


# -----------------------------
# Object Creation and Operations
# -----------------------------

s1 = Sorted_lst()
s1.add(10)
s1.add(1)
s1.add(11)
s1.add(3)
s1.add(2)

# Display the automatically sorted list
s1.display()     # ✅ Output: [1, 2, 3, 10, 11]

# Continuing with the previous Sorted_lst class

# Display the current sorted list
s1.display()             # Output: [1, 2, 3, 10, 11]

# -----------------------------
# Checking insertion position for a new value
# -----------------------------
print(s1.insert_pos(4))  # Output: 3 → 4 would fit between 3 and 10


# -----------------------------
# Removing an element (3) and displaying list
# -----------------------------
s1.remove(3)             # Removes value 3 from list
s1.display()             # Output: [1, 2, 10, 11]

# Now check again where 4 should be inserted
print(s1.insert_pos(4))  # Output: 2 → Now 4 fits between 2 and 10


# -----------------------------
# Trying to remove 3 again (will cause ValueError)
# -----------------------------
s1.remove(3)             # ❌ ERROR: 3 no longer exists in list
s1.display()
