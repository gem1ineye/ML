import random   # Import Python's built-in random module for pseudo-random number generation

# -----------------------------------------
# Random Floating-Point Numbers
# -----------------------------------------
print(random.random())     # Generates a random float in range [0.0, 1.0)
print(random.random())     # Each call gives a different random value

# -----------------------------------------
# Random Float within a Specific Range
# -----------------------------------------
print(random.uniform(1, 10))   # Returns a float between 1 and 10 (both inclusive)

# -----------------------------------------
# Random Integers
# -----------------------------------------
print(random.randint(1, 10))   # Returns an integer between 1 and 10 (both inclusive)

# -----------------------------------------
# Random Range (like range() but random)
# -----------------------------------------
print(random.randrange(1, 10, 2))   # Randomly picks an odd number between 1 and 9

# -----------------------------------------
# Seeding the Random Number Generator
# -----------------------------------------
# By default, random() uses system time for seeding → changes every run
# If we fix the seed, we get the SAME sequence of random numbers every time.
random.seed(10)

print(random.random())    # All following values are now deterministic
print(random.random())
print(random.random())

# Reset the seed to 10 → same sequence repeats
random.seed(10)
print(random.random())
print(random.random())
print(random.random())

# -----------------------------------------
# Random Choice from a Sequence
# -----------------------------------------
L = [1, 3, 5, 6, 7, 8]
print(random.choice(L))   # Randomly selects one element from list L

L = ['Ajay', 'Priya', 'Mridul', 'Ganga']
print(random.choice(L))   # Picks one random name from the list

# -----------------------------------------
# Shuffling a List
# -----------------------------------------
print(random.shuffle(L))  # Shuffles elements of list L in place (returns None)
print(L)                  # Check shuffled order

# -----------------------------------------
# Saving and Restoring Random Generator State
# -----------------------------------------
random.random()           # Generate some randoms
st = random.getstate()    # Save the current internal state of RNG

# Generate few more random numbers
print(random.random())
print(random.random())
print(random.random())

# Restore the RNG state
random.setstate(st)

# These three values will repeat previous ones
print(random.random())
print(random.random())
print(random.random())

# -----------------------------------------
# Generate Random Bits
# -----------------------------------------
print(random.getrandbits(3))   # Generates a random integer using 3 random bits (range: 0–7)
