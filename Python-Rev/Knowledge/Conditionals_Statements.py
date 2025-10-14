# -------------------------------
# LEXICOGRAPHIC (DICTIONARY) ORDER
# -------------------------------
# In Python, strings are compared character by character based on their Unicode values.
# Numbers come before uppercase letters, and uppercase letters come before lowercase letters.
if ('2nd' > 'Byte'):
    print(True)   # Will print True because '2' (Unicode 50) < 'B' (Unicode 66), so comparison flips
else:
    print(False)

# -------------------------------
# OBJECT IDENTITY CHECK
# -------------------------------
a = 10
b = 10.0
print(id(a), id(b))  
# 'a' and 'b' have different ids because one is int (10) and the other is float (10.0)

# -------------------------------
# INFINITY VALUES
# -------------------------------
max = float('inf')   # Represents positive infinity
min = float('inf')   # Same here, but usually for minimum we use float('-inf')
print(max)           # Output: inf

# -------------------------------
# WHILE-ELSE LOOP
# -------------------------------
# The 'else' part of a while loop runs only when the loop condition becomes False
# (and NOT when you break out of the loop)
while (a < 11):      # Loop runs as long as 'a' < 11
    print(a)
    a = a + 1
else:
    print('Khatam')  # Runs after the while loop finishes naturally

# -------------------------------
# RANGE FUNCTION DEMO
# -------------------------------
print(range(5))       # Prints the range object → range(0, 5)
