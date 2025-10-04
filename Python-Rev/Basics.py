# -------------------------------
# PRINTING A STRING
# -------------------------------
print('Hello-World')  # Simply prints the text "Hello-World"

# -------------------------------
# MULTIPLE VARIABLE ASSIGNMENT
# -------------------------------
a, b, c = 10, 20, 30
print(a, b, c)  # Prints: 10 20 30

# -------------------------------
# COMPLEX NUMBERS
# -------------------------------
dp = 7 + 6j
print(type(dp))  # Output: <class 'complex'>

# -------------------------------
# LARGE NUMERIC LITERALS WITH UNDERSCORES
# -------------------------------
# Improves readability; Python ignores underscores in numbers
d = 123_45_9.
print(d)  # Output: 123459.0

# -------------------------------
# TYPE CONVERSION
# -------------------------------
print(type(int('23')))  # Converts string "23" to integer → <class 'int'>

# -------------------------------
# BOOLEAN WITH COMPLEX NUMBERS
# -------------------------------
# bool(x+yj) is False only if both real and imaginary parts are zero
print(bool(0+6j))  # Output: True (because imaginary part ≠ 0)

# -------------------------------
# DIVISIONS
# -------------------------------
print(14 // 4)  # Floor division → 3 (integer division, rounds down)
print(14 / 4)   # Normal division → 3.5 (float result)
print(14 % 4)   # Modulus → 2 (remainder when 14 divided by 4)

# -------------------------------
# EXPONENTIATION
# -------------------------------
print((2**3)**2)  # (2^3)^2 = 8^2 = 64
print(2**3**2)    # 2^(3^2) = 2^9 = 512 (right-to-left associativity)

# -------------------------------
# STRING REPLICATION
# -------------------------------
print('abc' * 7)  # Repeats 'abc' 7 times → 'abcabcabcabcabcabcabc'

# -------------------------------
# POWER EXAMPLE
# -------------------------------
print(2**8)  # 2^8 = 256
