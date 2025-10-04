'''
Does traceback mean runtime error?
👉 Yes. A traceback appears when a runtime error (exception) occurs.
   Example: dividing by zero, accessing invalid index, etc.
'''

a, b = 10, 1

try:
    # Risky operation
    c = a / b
    print(c)
except:
    # This block runs if an error occurs
    print('❌ You divided it by zero, change it!')


print('end')   # This will always run after try/except

#Handling Multiple Exception

Lst=[10,20,30,40,50]


try:
    
    print(Lst[1])
except IndexError:
    print('Saale index aukaat ke bhaar ka mat daal')
except TypeError:
    print('yeh tune number daala hai 4thi fail hai kya')
    
    

try:
    index=1
    print(Lst[index])
except IndexError as msg:
    print(msg)


def fun(a,v):
    if v!=0:
        c=a//v
        return c
    else:
        raise ZeroDivisionError

try:
    res=fun(10,0)
    print(res)
except:
    print('Zero division error')
    

# Try-Except-Else Example
a = 10
b = 0

try:
    # Only the risky part goes here
    c = a // b        # ❌ Division by zero → raises exception
except:
    # This runs if error occurs
    print('⚠️ Error: Division by zero')
else:
    # This runs only if try block succeeds without error
    print(c)

'''
✅ Best Practice:
- Keep only the code that might cause error inside try.
- Put the rest (safe code) inside else.
- That way, debugging becomes easier and clean.
'''


def gun():
    try:
        x = int('256')   # ✅ Valid conversion, no error
        return x         # Function tries to return here
    except Exception as e:
        # If error occurs, it will come here
        # and re-raise the same error
        raise e
    finally:
        # This block ALWAYS executes
        # (even if return happened or exception raised)
        print('✅ Mein toh hamesha run karunga!')

print(gun())

# User Defined Exception
class NegativeError(Exception):
    """Custom Exception for handling negative values"""
    pass

def area(l, b):
    if l >= 0 and b >= 0:
        return l * b
    else:
        # Raise our custom exception if dimensions are negative
        raise NegativeError("❌ Negative dimension not allowed")

# Calling function
print(area(9, -7))   # This will raise NegativeError
