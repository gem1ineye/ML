import copy

# -----------------------------------------
# Python: Shallow Copy vs Deep Copy
# -----------------------------------------
# The copy module provides two important functions:
# ✅ copy.copy()  → Shallow Copy (copies outer structure)
# ✅ copy.deepcopy() → Deep Copy (copies entire object graph)

# -----------------------------------------
# Simple list example (shallow copy)
# -----------------------------------------
l = [10, 20, 30, 40, 50, 60]

# Shallow copy → creates a new list object,
# but elements inside still refer to the same objects as original.
l1 = copy.copy(l)

print("Original list:", l)
print("Copied list:", l1)

# Check identity (outer object)
print("ID of l :", id(l))    # Different
print("ID of l1:", id(l1))   # Different

# Check identity (inner objects — elements)
print("ID of l[0]:", id(l[0]))    # Same
print("ID of l1[0]:", id(l1[0]))  # Same → shared reference

# Modify copied list element
l1[0] = 77  # Changing an element creates a new reference in l1 only

# Recheck IDs after modification
print("After modification:")
print("ID of l[0]:", id(l[0]))    # Unchanged
print("ID of l1[0]:", id(l1[0]))  # Different now

# -----------------------------------------
# Deep Copy Example (with Class Objects)
# -----------------------------------------
class Person:
    def __init__(self, name):
        self.name = name

# List of objects
C = [Person('John'), Person('Max')]

# Deep copy → duplicates both the outer list and all contained objects
C1 = copy.deepcopy(C)

print("ID of original list (C):", id(C))
print("ID of deep copied list (C1):", id(C1))

# Verify individual object references are different
print("ID of C[0]:", id(C[0]))
print("ID of C1[0]:", id(C1[0]))
