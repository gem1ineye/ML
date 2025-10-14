# -----------------------------
# Iterators
# -----------------------------
l1 = [1, 2, 3, 4, 5]

# iter() converts an iterable (like list, tuple, set, etc.) into an iterator object
it = iter(l1)

# next() returns the next element from the iterator
# Each call advances the internal pointer
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# (further next(it) would give 4,5, then StopIteration error)


# -----------------------------
# Generators
# -----------------------------
# A generator is a special kind of iterator created with "yield"
# It produces values one at a time and remembers its state between calls

def myrange(n):
    i = 0
    while i < n:
        yield i   # yield pauses function and returns a value
        i = i + 1 # when resumed, execution continues from here


# Create generator object
m = myrange(5)

# next() fetches next yielded value from generator
print(next(m))  # 0
print(next(m))  # 1
print(next(m))  # 2
print(next(m))  # 3
print(next(m))  # 4
# Next call will raise StopIteration because generator is exhausted


#Generator for Days in Week

def days():
    d=['sun','mon','tue','wed','thu','fri','sat']
    i=0
    while True:
        yield(d[i])
        i=(i+1)%7

