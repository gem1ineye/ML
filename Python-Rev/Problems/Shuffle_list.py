import random as rd

# -----------------------------
# random() 
# -----------------------------
# Returns a random float between 0.0 and 1.0
print(rd.random())        # Example: 0.67283912


# -----------------------------
# randint(a, b)
# -----------------------------
# Returns a random integer N such that a <= N <= b
# ⚠️ You must provide TWO arguments (start, end)
print(rd.randint(1, 10))  # Example: 7

lst = [10, 11, 13, 14, 19]

print(rd.shuffle(lst))
print(lst)