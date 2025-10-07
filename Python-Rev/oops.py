class Rectangle:
    def __init__(self, length, breadth): # __init__ is a constructor, it runs when object is created
        print(('Self id: ',id(self)))
        self.len = length                       # storing length in object (self)
        self.breadth = breadth                  # storing breadth in object (self)
        
    def area(self):                             # method to calculate area
        return self.len * self.breadth
    
    def perimeter(self):                        # method to calculate perimeter
        return 2 * (self.len + self.breadth)

# creating object of Rectangle class
r = Rectangle(3, 5)

# calling area method
print(r.area())    # Output: 15
print('r object id: ',id(r))