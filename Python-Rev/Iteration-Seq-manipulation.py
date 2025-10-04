list1 = [1, 12, 7, -3, 8]

# -----------------------------
# sorted() → returns a new sorted list (does not change original)
# -----------------------------
print(sorted(list1))                     # [-3, 1, 7, 8, 12] → ascending
print(sorted(list1, reverse=True))       # [12, 8, 7, 1, -3] → descending
print(sorted(list1, key=abs))            # [1, -3, 7, 8, 12] → sorted by absolute values


# -----------------------------
# reversed() → returns an iterator that iterates in reverse
# -----------------------------
rev = reversed(list1)
print(list(rev))   # [8, -3, 7, 12, 1]


# -----------------------------
# slice(start, stop, step) → creates a slice object
# Useful when slicing lists, strings, tuples
# -----------------------------
s = slice(5)   # equivalent to [:5] → from 0 to index 4
list2 = [10, 20, 30, 40, 50, 60, 70]
print(list2[s])   # [10, 20, 30, 40, 50]
