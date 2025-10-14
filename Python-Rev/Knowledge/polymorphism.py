# -----------------------------
# Polymorphism Example
# -----------------------------
# Polymorphism = "Same name, different behavior"
# Here, the same function 'sum' works for multiple data types (tuple, list, set)
# because they all are iterable and can be looped through.

def sum(seq):
    s = 0
    for x in seq:        # works for any iterable (list, tuple, set, etc.)
        s += x
    return s


# Calling 'sum' function with different data types
print(sum((1, 2, 3)))     # Tuple input  → Output: 6
print(sum([1, 3, 5, 7]))  # List input   → Output: 16
print(sum({1, 3, 4, 5}))  # Set input    → Output: 13


# -----------------------------
# Duck Typing in Python
# -----------------------------
# "If it walks like a duck and talks like a duck, it’s a duck."
# In Python, we don't care about the object's actual class —
# we only care whether it has the required methods (talk, walk).

class Duck:
    def __init__(self):
        pass
    
    def talk(self):
        print('Duck Talking')
    
    def walk(self):
        print('Duck walking')


class Dog:
    def __init__(self):
        pass
    
    def talk(self):
        print('Dog Talking')
        
    def walk(self):
        print('Dog Walking')


# Function that accepts any object having 'talk' and 'walk' methods
def person(pet):
    # Doesn't check type — only that object supports required behavior
    pet.talk()
    pet.walk()


# Creating Dog object
dog = Dog()
person(dog)    # ✅ Works because Dog has talk() and walk()

# Creating Duck object
duck = Duck()
person(duck)   # ✅ Works too because Duck also has talk() and walk()



# -----------------------------------------
# Method Overloading in Python
# -----------------------------------------
# Overloading means: multiple methods with the same name but different parameters.
# ⚠️ However, Python does NOT support true method overloading like Java or C++.
# The latest defined function with the same name overrides the previous ones.

# (a) By passing different data types
def sum(a, b):
    # Works for numbers, strings, floats, etc.
    return a + b


# Calling the same function with different data types
print(sum(1, 2))            # integers → Output: 3
print(sum('Hello', 'World'))# strings → Output: HelloWorld
print(sum(1.2, 0.34))       # floats  → Output: 1.54


# (b) By passing multiple parameters
# Defining another 'sum' function (same name)
def sum(a, b, c):
    # This definition OVERRIDES the previous one completely
    return a + b + c


# Now, only this version of 'sum' exists — the earlier one is lost
print(sum(1, 2, 3))         # Output: 6

# Method Overriding

class Parent:
    def show(self):
        return "Calling from parent class"
    

class Child(Parent):
    def show(self):                        #Here child class show function overriding parent class show function.
        return "calling from child class"

c=Child()
print(c.show())

# -----------------------------------------
# Method Overriding with super()
# -----------------------------------------
# When a child class defines a method with the same name as one in its parent class,
# it overrides (replaces) the parent's version during runtime.

class Parent:
    def show(self):
        return "Calling from parent class"   # Parent class method


class Child(Parent):
    def show(self):                          
        # 'super()' calls the parent class method with the same name
        return super().show()                # Accessing overridden method from Parent
        
        # This line will never execute because the function returns above
        return "Calling from child class"    # (unreachable code)


# --- Object Creation and Testing ---
c = Child()

# Calls the overridden method from Child class
# Since super().show() is called, it executes Parent's show() instead
print(c.show())      # ✅ Output: Calling from parent class


# -----------------------------------------
# Operator Overloading
# -----------------------------------------
# In Python, operators like +, -, *, etc. are implemented using special methods.
# For example:
#   +  →  __add__()
#   -  →  __sub__()
#   *  →  __mul__()
#   == →  __eq__()
# This allows custom objects to define their own behavior for these operators.

class Vector:
    def __init__(self, x, y):
        # Initializing x and y coordinates of the vector
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """
        ✅ Overloading the '+' operator.
        This allows two Vector objects to be added using '+'.
        """
        x = self.x + other.x     # Add corresponding x-coordinates
        y = self.y + other.y     # Add corresponding y-coordinates
        return Vector(x, y)      # Return a new Vector object as the result
    
    def __str__(self):
        """
        ✅ String representation for easy printing of Vector objects.
        Without this, printing would show a memory address.
        """
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


# --- Object Creation ---
v1 = Vector(1, 2)
v2 = Vector(4, 5)

# '+' automatically calls __add__()
v3 = v1 + v2

# Print the result (automatically calls __str__())
print('Vector Sum:', v3)    # Output: Vector Sum: (5, 7)


# Specialization means  Inheritance

# Generalizatiion menas polymorphism

# -----------------------------------------
# Abstract Class and Interface in Python
# -----------------------------------------
# Abstract classes are blueprints for other classes.
# They can define methods that must be implemented by any subclass.
# Python provides this feature through the 'abc' (Abstract Base Class) module.

from abc import ABC, abstractclassmethod

# -----------------------------------------
# Abstract Base Class
# -----------------------------------------
class P1(ABC):                     # Inheriting from ABC makes this an abstract class
    def meth1(self):
        # A normal method (can be inherited directly by child)
        print('Parent meth--1')
    
    @abstractclassmethod
    def meth2(self):
        # Abstract method → must be implemented by child class
        pass


# -----------------------------------------
# Concrete (Child) Class
# -----------------------------------------
class C1(P1):
    def meth3(self):
        # Additional method defined only in child
        print('Child meth--3')
    
    # Overriding the abstract method (mandatory)
    def meth2(self):
        print('Calling meth2 from C1')


# -----------------------------------------
# Object Creation and Method Call
# -----------------------------------------
c = C1()          # ✅ Allowed (C1 implements all abstract methods)
c.meth2()         # Output: Calling meth2 from C1



# -----------------------------------------
# Method Resolution Order (MRO)
# -----------------------------------------
# MRO defines the order in which Python looks for a method
# in a hierarchy of classes (especially useful in multiple inheritance).

from abc import ABC

# -----------------------------------------
# Parent Class
# -----------------------------------------
class P2(ABC):                     
    def show(self):
         print('Parent')

# -----------------------------------------
# Child Class
# -----------------------------------------
class C2(P2):
    def show(self):
        # Overriding the parent's show() method
        print('Child')

# -----------------------------------------
# Object Creation and Testing
# -----------------------------------------
child = C2()

# Calls the show() method
# Since 'C2' overrides it, the child version executes first
child.show()            # Output: Child

# -----------------------------------------
# Checking Method Resolution Order
# -----------------------------------------
print(C2.mro())
# .mro() → returns the order in which classes are searched for methods.
# Output: [<class '__main__.C2'>, <class '__main__.P2'>, <class 'abc.ABC'>, <class 'object'>]
# Order means:
#    1. Look in C2 (child)
#    2. Then in P2 (parent)
#    3. Then in ABC (since P2 inherits it)
#    4. Finally in object (top-most Python base class)

