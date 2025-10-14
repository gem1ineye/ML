# -------------------------------
# BASIC FOR LOOP WITH range()
# -------------------------------
for i in range(5):
    print(i, end=' ')  # Prints numbers 0 to 4 in one line
print('')  # Just prints a newline

# -------------------------------
# ITERATING OVER A STRING
# -------------------------------
for i in 'harsh':
    print(i, end=' ')  # Prints each character of the string
print(' ')  # Newline for spacing

# -------------------------------
# USING range(start, stop, step)
# -------------------------------
for i in range(2, 10, 3):  # Start=2, Stop=10, Step=3
    print(i, end=' ')  # Prints: 2 5 8
print('')  # Newline

# -------------------------------
# FIBONACCI SERIES USING LOOP
# -------------------------------
print("Fibonacci Series:")

a = 0
b = 1
print(a, b, end=' ')  # Print first two Fibonacci numbers

c = 0
for x in range(5):  # Generate next 5 Fibonacci numbers
    print(a + b, end=' ')
    c = a           # Store current 'a' in 'c'
    a = b           # Move 'b' to 'a'
    b = c + b       # Calculate next Fibonacci number
