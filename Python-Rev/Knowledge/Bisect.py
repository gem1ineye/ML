# -----------------------------------------
# Python: bisect module (Binary Search Utilities)
# -----------------------------------------
# The bisect module helps maintain a sorted list.
# It allows insertion and searching using binary search.
# ✅ Ideal for sorted lists to insert new items while keeping order.

import bisect

# -----------------------------------------
# Initial sorted list
# -----------------------------------------
l = [20, 30, 40, 50]
print("Initial list:", l)

# -----------------------------------------
# Insert element (left insertion)
# -----------------------------------------
# insort_left(list, item)
# Inserts item in sorted order — before any existing entries of the same value
bisect.insort_left(l, 70)
print("After insort_left(70):", l)

# -----------------------------------------
# Insert element (right insertion)
# -----------------------------------------
# insort_right(list, item)
# Inserts item in sorted order — after any existing entries of the same value
bisect.insort_right(l, 70)
print("After insort_right(70):", l)

# -----------------------------------------
# Find position where item should be inserted
# -----------------------------------------
# bisect(list, item)
# Returns the insertion index (as if insort_right was called)
pos = bisect.bisect(l, 9)
print("Insertion position for 9:", pos)
