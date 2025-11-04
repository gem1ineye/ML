import fractions    # Import the fractions module for rational number arithmetic

# -----------------------------------------
# Creating Fraction objects
# -----------------------------------------
f1 = fractions.Fraction(1, 2)       # Fraction with numerator=1, denominator=2 → represents 1/2
print(f1)                           # Output: 1/2
print('{}'.format(f1))              # Prints same value using string formatting

# -----------------------------------------
# Creating a Fraction from a floating-point number
# -----------------------------------------
f2 = fractions.Fraction(0.2)        # Automatically converts 0.2 into an exact fraction
print(f2)                           # Output: 3602879701896397/18014398509481984 (internal binary representation)

# Limit denominator to make the fraction more readable
f2 = f2.limit_denominator(10)       # Approximate 0.2 as a simple fraction with denominator ≤ 10
print(f2)                           # Output: 1/5

# -----------------------------------------
# Another fraction from a float
# -----------------------------------------
f3 = fractions.Fraction(0.3)
print(f3)                           # Output: 5404319552844595/18014398509481984

# -----------------------------------------
# Performing Arithmetic Operations
# -----------------------------------------
# Fractions module supports +, -, *, / directly (keeps result as Fraction)
print('{}'.format(f1 - f2))         # Subtraction → (1/2 - 1/5 = 3/10)
print('{}'.format(f1 + f2))         # Addition → (1/2 + 1/5 = 7/10)
print(f1 * f2)                      # Multiplication → (1/2 * 1/5 = 1/10)
print(f1 / f2)                      # Division → (1/2 ÷ 1/5 = 5/2)

x=True

l=[]
l.pop()