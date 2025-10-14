# -----------------------------
# type() → shows the exact type of an object
# isinstance(obj, class) → checks if obj is an instance of a class (or tuple of classes)
# -----------------------------

print(type([1,2,3]))    # <class 'list'>
print(type((1,2,3)))    # <class 'tuple'>
print(type(1))          # <class 'int'>
print(type(1.89))       # <class 'float'>

print(isinstance([1,2,3], list))     # True  → it's a list
print(isinstance(0, int))            # True  → it's an int
print(isinstance(0, (int, str)))     # True  → 0 is int (matches one of the tuple types)


# -----------------------------
# hasattr(object, attribute_name)
# Checks if the object has the given attribute/method
# -----------------------------

text = 'Hello'

print(hasattr(text, 'lower'))   # True  → str objects have a .lower() method
print(hasattr(text, 'search'))  # False → str does NOT have .search()


import math

# -----------------------------
# getattr(object, attribute_name)
# -----------------------------
# Returns the value of an attribute from a module/class/object by name (string)
print(getattr(math, 'pi'))        # 3.141592653589793
print(getattr(math, 'sqrt')(25))  # 5.0 → calls math.sqrt(25)


# -----------------------------
# id(object)
# -----------------------------
# Returns the unique memory address (ID) of an object
x = 10
y = 10
print(id(x))   # ID of x
print(id(y))   # Same as x because Python reuses small integers


# -----------------------------
# dir(object)
# -----------------------------
# Shows all attributes & methods of an object, class, or module
print(dir(list))   # methods/attributes of list
print(dir(math))   # functions & constants in math module


# -----------------------------
# repr(object)
# -----------------------------
# Returns a developer-friendly string representation of an object
text = 'Hello'
print(repr(text))   # 'Hello' → includes quotes, unlike print(text)
