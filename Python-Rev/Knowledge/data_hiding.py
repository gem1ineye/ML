# Inheritance and Name Mangling Example

class Parent:
    
    def __init__(self, d):
        self._data = d           # double underscore (__) makes 'data' a private variable
                                  # single underscore (_) makes 'data' a protected variable
    
    def show(self):
        print(self._data)        # can access private variable inside the class


# Creating object of Parent class
p = Parent(10)
p.show()                         # ✅ prints 10 (accessing private variable through public method)


# Name Mangling: forcibly accessing private data outside the class
p._Parent_data = 20             # this is not recommended, but Python allows it by changing variable name internally
p.show()                         # ✅ prints 20 (shows that private data can still be modified using name mangling)


# Creating a Child class (not inheriting Parent here)
class Child(Parent):
    def __init__(self, d):           # constructor of Child class
        super().__init__(d)    # ❌ incorrect call — super() used but Parent not inherited
    
    def display(self):
        print(self._data)           # ❌ will cause error because __data is private to Parent class


# Creating object of Child class
c = Child(25)
c.show()                             # ❌ will give error — Child doesn’t inherit Parent’s show() method




# Example of a Nested Class (Class inside another class)

class B:
    def __init__(self):
        # Creating an object of inner class A inside class B’s constructor
        self.a_obj = self.A()
        
    def show(self):
        # Calling method of inner class A using the created object
        self.a_obj.display()
    
    # Inner (nested) class A
    class A:
        def __init__(self):
            # Initializing variable inside inner class
            self.l1 = 'class A is called'
        
        def display(self):
            # Printing message from inner class
            print(self.l1)


# Creating an object of outer class B
outer = B()

# Calling outer class method which internally calls inner class method
outer.show()      # ✅ Output: class A is called

        