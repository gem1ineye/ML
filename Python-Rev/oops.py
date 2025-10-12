class Rectangle:
    
    count = 0   # ✅ Class variable — shared among all objects of the class
    
    def __init__(self, length, breadth):
        """
        __init__() is the constructor.
        It initializes the object with length and breadth whenever a new object is created.
        """
        print(('Self id:', id(self)))  # Prints the memory location (unique ID) of the current object
        
        # Instance variables — unique for each object
        self.len = length
        self.breadth = breadth
        
        # Incrementing class variable (shared counter for all Rectangle objects)
        Rectangle.count += 1
    
    def area(self):
        """Returns the area of the rectangle (instance method)"""
        return self.len * self.breadth
    
    def perimeter(self):
        """Returns the perimeter of the rectangle (instance method)"""
        return 2 * (self.len + self.breadth)
    
    @staticmethod
    def calc_area(length, breadth):
        """
        ✅ Static Method:
        This method does not depend on instance (self) or class (cls).
        It behaves like a normal function but belongs to the class namespace.
        We dont have to create an object for accessing static method
        Useful for utility calculations.
        """
        return length * breadth

    @classmethod
    def get_class_count(cls):
        """
        ✅ Class Method (uses 'cls' instead of 'self'):
        It can access or modify class-level data like 'count'.
        """
        return cls.count


# --- Object Creation & Method Calls ---

# Creating an object of Rectangle class
r = Rectangle(3, 5)

# Calling the instance method 'area'
print(r.area())     # Output: 15

# Printing the memory address of object 'r'
print('r object id:', id(r))

# Calling the class method — counts total Rectangle objects created
print('Total Rectangles created:', Rectangle.get_class_count())

# Calling the static method directly using class name (no object needed)
print('Area using static method:', Rectangle.calc_area(3, 4))   # Output: 12



class Circle:
    
    def __init__(self, r):
        # When we assign to 'self.radius', it automatically calls the @radius.setter method
        self.radius = r
    
    @property
    def radius(self):
        """
        ✅ Getter Method:
        Allows you to access 'radius' like an attribute (c.radius) 
        while still controlling access internally.
        Returns the value of the private variable '_radius'.
        """
        return self._radius
    
    @radius.setter
    def radius(self, r):
        """
        ✅ Setter Method:
        This runs automatically when 'radius' is assigned a value.
        It validates input — ensures radius cannot be negative.
        """
        if r >= 0:
            self._radius = r
        else:
            # If radius is negative, default it to 1
            self._radius = 1
    
 

# --- Object Creation & Testing ---



c = Circle(3)       # Calls __init__ → sets radius = 3 (via setter)
c.radius = -2       # Triggers setter → replaces -2 with 1
print(c.radius)     # Calls getter → prints 1


