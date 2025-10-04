# -----------------------------
# Assigning built-in functions to variables
# -----------------------------

show = print   # alias for print()
show('hello')  # works same as print('hello')

'''
take = input   # alias for input()
x = take('enter the num: ')  # same as input('enter the num: ')

print("You entered:", x)
'''

# -----------------------------
# Nested Functions (Function inside another function)
# -----------------------------

def Outer():
    # Inner function defined inside Outer
    def Inner():
        print('Calling from Inner')  
        # Inner() can only be called inside Outer(), 
        # it’s not accessible directly from outside
    
    print('Calling from Outer')
    
    Inner()  # calling Inner function inside Outer


# Call the outer function
Outer()


#Function as parameter

# -----------------------------
# Passing Functions as Arguments (Higher-Order Functions)
# -----------------------------

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

# arithmetic() takes a function 'f' and applies it on (x, y)
def arithmetic(f, x, y):
    return f(x, y)


# Passing 'add' function
sun = arithmetic(add, 4, 5)   # calls add(4, 5)
print(sun)  # 9

# Passing 'sub' function
su = arithmetic(sub, 7, 4)    # calls sub(7, 4)
print(su)  # 3



# -----------------------------
# Returning a Function from Another Function
# -----------------------------

def outer():
    def inner():
        print('Hello')
    return inner   # returning the function (not calling it)


# outer() returns inner → so fun now refers to inner()
fun = outer()

# Calling the returned function
fun()   # Output: Hello

# -----------------------------
# Closure Example
# -----------------------------
# A closure is when an inner function "remembers" variables
# from its enclosing (outer) function, even after the outer function has finished.
# -----------------------------

def get_counter():
    count = 0               # local variable in outer function

    def counter():
        nonlocal count      # allows modifying 'count' from outer scope
        count += 1
        return count
    
    return counter          # return the inner function


# Each call to get_counter() creates a new independent closure
c1 = get_counter()
c2 = get_counter()

# c1 has its own 'count'
print(c1(), c1(), c1())   # 1 2 3

# c2 has a separate 'count'
print(c2(), c2(), c2())   # 1 2 3

# -----------------------------
# Decorator Function
# -----------------------------
# A decorator is basically:
#   Closure (inner function) + Function as parameter
# -----------------------------

def Outer(f):   # f = function to decorate
    def Inner():
        print('+' * 10)   # extra behavior before
        f()               # original function call
        print('+' * 10)   # extra behavior after
    return Inner          # return decorated function


# Instead of: display = Outer(display)
# We can use the decorator shortcut:
@Outer
def display():
    print("hell Yeah")


# Now calling display() actually calls Inner()
display()

# Lambda examples
k = lambda x: x * 2
print(k(2))                   # 4

son = lambda x, y: x + y
print(son(9, 9))              # 18

print((lambda k: k * 4)(5))   # 20 (lambda used inline)

# Filter example → keep only multiples of 3
list1 = [1, 2, 3, 6, 9, 12, 4]
f = filter(lambda x: x % 3 == 0, list1)
print(list(f))                # [3, 6, 9, 12]

# Map example → convert to negatives
l1 = [1, 2, 3, 4]
l2 = map(lambda x: -x, l1)
print(list(l2))               # [-1, -2, -3, -4]

# Map with condition → even = keep, odd = make negative
l3 = [1,2,3,4,5,6,7,8,9,10]
k = lambda x: x if x % 2 == 0 else -x
list2 = list(map(k, l3))
print(list2)                  # [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

# Caller Class Example
class Day:
    def __init__(self):
        # Dictionary mapping numbers to day names
        self.days = {
            0: 'Sunday', 
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Sunday'
        }
    
    # __call__() makes the object behave like a function
    def __call__(self, dayno):
        return self.days[dayno]

# Create object of class Day
d = Day()

# Instead of calling a method, we call the object directly
print(d(3))       # caller class means class object treated as function.

        