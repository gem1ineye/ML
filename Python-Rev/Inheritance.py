# ✅ Inheritance: Borrowing features (attributes and methods) from an existing class

class Rectangle:
    def __init__(self, l, b):
        # Instance variables for Rectangle
        self.length = l
        self.breadth = b
    
    def Area(self):
        """Returns the area of the rectangle"""
        return self.length * self.breadth
    
    def Perimeter(self):
        """Returns the perimeter of the rectangle"""
        return 2 * (self.length + self.breadth)


# ✅ 'Cuboid' is a child (derived) class that inherits from 'Rectangle'
class Cuboid(Rectangle):
    
    def __init__(self, l1, b1, h):
        # Child class has an additional property 'height'
        self.height = h
        
        # 'super()' calls the parent class constructor to initialize length and breadth
        super().__init__(l1, b1)
        
    def vol(self):
        """Returns the volume of the cuboid"""
        return self.length * self.breadth * self.height


# --- Object Creation & Method Calls ---

c = Cuboid(1, 2, 3)

# Using child class method
print("Volume of Cuboid:", c.vol())    # Output: 6
