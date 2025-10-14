# -----------------------------
# Built-in Math Functions
# -----------------------------

# abs(x) → returns the absolute (positive) value of a number
print(abs(-70))        # 70  (negative becomes positive)
print(abs(4+4j))       # 5.656854249492381 → sqrt(4² + 4²)

# pow(x, y) → returns x raised to the power y
print(pow(2, 3))       # 2³ = 8

# pow(x, y, z) → (x ** y) % z  (modular exponentiation)
print(pow(10, 2, 3))   # (10²) % 3 = 100 % 3 = 1


# -----------------------------
# round(x) → rounds to nearest integer
# -----------------------------
# Python uses **Banker's Rounding**:
# - If the number is exactly halfway (.5), it rounds to the nearest EVEN integer.

print(round(4.5))   # 4 → (4.5 is exactly halfway, nearest even is 4)
print(round(5.5))   # 6 → (5.5 is exactly halfway, nearest even is 6)

 
# -----------------------------
# Built-in Utility Functions
# -----------------------------

# divmod(a, b) → returns a tuple (quotient, remainder)
print(divmod(10, 3))   # (3, 1) → 10 ÷ 3 = 3 remainder 1


# -----------------------------
# min() and max()
# -----------------------------
print(min(10, 3, 4, 2, 3))         # 2 → smallest value
print(min(10, 2, -4, 9, -99))      # -99 → smallest value

# key=abs → compares by absolute value
print(min([1, 2, 3, 4, -8, -2], key=abs))  # -2 → smallest absolute value is 2

keys = ['hell', 'monster', 'coke']
print(max(keys, key=len))          # "monster" → longest string


# -----------------------------
# sum()
# -----------------------------
print(sum([1, 2, 3, 4, 5]))            # 15 → 1+2+3+4+5
print(sum([1, 2, 3, 4, 5], start=20))  # 35 → starts sum at 20


# -----------------------------
# eval(expression, globals=None, locals=None)
# -----------------------------
# eval() evaluates a string as a Python expression
print(eval('10+20*4-5'))    # 85 → 10 + (20*4) - 5

globals_dict = {
    'x': 5,
    'y': 45
}

locals_dict = {
    'z': 90
}

# Here eval can access x,y from globals_dict and z from locals_dict
print(eval('x + y + z', globals_dict, locals_dict))  # 5 + 45 + 90 = 140
