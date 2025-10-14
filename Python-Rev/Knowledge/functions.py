# -----------------------------
# Functions in Python
# -----------------------------

# Simple function without parameters
def fun():
    print('hello')


# Function with parameters and return value
# x, y → formal arguments (placeholders for input values)
def fun1(x, y):
    return x + y


# __name__ == '__main__' → runs this part only if script is executed directly
if __name__ == '__main__':
    print(fun1(2, 3))   # Output: 5


# Function with 3 parameters
def fun2(l, b, h):
    print(l * b * h)


# Positional arguments → values passed in order
fun2(1, 2, 3)          # Output: 6

# Keyword arguments → specify parameter names explicitly
fun2(b=10, l=2, h=5)   # Output: 100


# Function with positional-only arguments
def fun3(a, b, /, c, d):
    # a, b → must be passed as positional arguments
    # c, d → can be passed either as positional or keyword
    print(a, b, c, d)


# Example calls
fun3(1, 2, 3, 4)            # All positional
fun3(1, 2, c=30, d=40)      # Mix of positional and keyword


# -----------------------------
# Keyword-only arguments in Python
# -----------------------------

def fun4(a, b, *, c, d):
    # a, b → can be passed as positional OR keyword arguments
    # c, d → must be passed as keyword arguments (because of *)
    print(a, b, c, d)


# Example calls
fun4(1, 2, c=3, d=4)       # ✅ valid (a, b are positional, c, d are keyword)
fun4(a=10, b=20, c=30, d=40)  # ✅ valid (all keyword)
# fun4(1, 2, 3, 4)   ❌ Error (c and d must be keyword arguments)

# -----------------------------
# Combining Positional-only, Regular, and Keyword-only arguments
# -----------------------------

def fun5(a, b, /, c, d, *, e, f):
    # a, b → must be positional-only (before /)
    # c, d → can be passed either as positional or keyword
    # e, f → must be keyword-only (after *)
    print(a, b, c, d, e, f)


# Example calls:
fun5(1, 2, 3, 4, e=5, f=6)          # ✅ a,b = positional, c,d = positional, e,f = keyword
fun5(10, 20, c=30, d=40, e=50, f=60) # ✅ mix of positional + keyword
# fun5(a=1, b=2, c=3, d=4, e=5, f=6) ❌ ERROR (a,b cannot be keyword because they are before /)




# -----------------------------
# Variable-Length Positional Arguments (*args)
# -----------------------------
# *args → collects extra positional arguments into a tuple
# Useful when you don’t know in advance how many arguments will be passed
# -----------------------------

def Vfun1(a, b, *args):
    # a, b → normal required arguments
    # *args → captures remaining arguments as a tuple
    print(a, b, args)


def Vfun2(*args):
    # Only *args, so all inputs are collected into a tuple
    print(args, len(args))


# Example calls
# Vfun1(1)              ❌ ERROR: 'b' missing
Vfun1(1, True)           # a=1, b=True, args=()
Vfun1(1, 'Hello', True)  # a=1, b='Hello', args=(True,)


# Passing a list
L1 = [1, 2, 3]
Vfun2(L1)     # args = ([1, 2, 3],) → single element (the list itself)
Vfun2(*L1)    # args = (1, 2, 3)   → list unpacked into separate arguments


#Variable lenght Keyword Argument
def Kfun1(**kwargs):
    print(kwargs)

Kfun1(a=1,b=2,c=39)