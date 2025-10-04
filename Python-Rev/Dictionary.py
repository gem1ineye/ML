# -----------------------------
# Dictionaries in Python
# -----------------------------
# Dictionary = key:value pairs, enclosed in { }
# Keys must be unique and immutable (int, str, tuple, etc.)
# Values can be of any data type (int, list, set, tuple, complex, etc.)
# -----------------------------

d1 = {
    1: 'one',
    2: 'Two',
    3: 'Three'
}

print(type(d1))   # <class 'dict'>
print(d1[1])      # Access value using key -> 'one'


# Dictionary with multiple data types as values
d2 = {
    1: 3.5,               # float
    2: [1, 2, 3],         # list
    3: {'hi', 'hello'},   # set
    4: (5.9, 4.9, 3.7),   # tuple
    5: 2+7j               # complex number
}

print(d2)
# Output: {1: 3.5, 2: [1, 2, 3], 3: {'hello', 'hi'}, 4: (5.9, 4.9, 3.7), 5: (2+7j)}


# -----------------------------
# Methods of Creating Dictionaries
# -----------------------------

# M1: Using iterable pairs (list of tuples)
# Can also use: list of lists, tuple of tuples, etc.
d3 = dict([(1, 'one'), (2, 'two'), (3, 'Three')])
print(d3)   # {1: 'one', 2: 'two', 3: 'Three'}


# M2: Using zip() → pairs elements from two lists into key:value
L1 = [1, 2, 3, 4]
L2 = ['one', 'two', 'three', 'four']
d4 = dict(zip(L1, L2))
print(d4)   # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}


# M3: Using enumerate() → assigns index to each item in list
# start=2 → indexing starts from 2 instead of default 0
d5 = dict(enumerate(L2, start=2))
print(d5)   # {2: 'one', 3: 'two', 4: 'three', 5: 'four'}

# -----------------------------
# Dictionary Comprehension
# Syntax: {key:value for item in iterable}
# -----------------------------

# Example 1: Creating dictionary from list of tuples
lt1 = [(1, 'one'), (2, 'two'), (3, 'Three')]
dt1 = {x: y for x, y in lt1}
print(dt1)     # {1: 'one', 2: 'two', 3: 'Three'}


# Example 2: Creating dictionary using zip() of two lists
lis1 = [1, 2, 3, 4]
lis2 = ['one', 'two', 'three', 'four']
dt2 = {x: y for x, y in zip(lis1, lis2)}
print(dt2)     # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}


# Example 3: Using enumerate() to assign indexes as keys
dt3 = {x: y for x, y in enumerate(lis2, start=1)}
print(dt3)     # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

dt3.setdefault(5,6)
print(dt3)

dx={2:'woh'}

dt3.update(dx)
print(dt3)


D={1:'foo',2:'doo',3:'koo'}

for n in D:
    print(n)
