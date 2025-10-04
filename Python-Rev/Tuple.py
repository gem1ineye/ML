#Tuple is same as list but it is immutable

# -----------------------------
# Ways of Creating Tuples
# -----------------------------

# Empty tuple
t1 = ()
print(type(t1))    # <class 'tuple'>


# Using tuple() constructor
t2 = tuple([1, 2, 3, 4, 5, 4])   # list converted into tuple
print(type(t2))    # <class 'tuple'>
print(t2)          # (1, 2, 3, 4, 5, 4)


# Directly creating tuple with parentheses
t3 = (1, 2, 3)
print(type(t3))    # <class 'tuple'>


# ⚠️ Special case: Single-element tuple
t4 = (1,)   # Comma is required, otherwise it's just an integer
print(t4)   # (1,)

t5=tuple(range(1,10,2))
print(t5)


tup=tuple(x for x in range(1,10) if(x%2==0))

print(tup)

z1=(1,2,3,4,5)

print(z1[-5:-1])

print(z1*2)

q1=1,2,3,4,5   #This is called packing and python make it as tuple

print(type(q1))

# -----------------------------
# Tuple Unpacking
# -----------------------------

# Creating a tuple (parentheses are optional)
T1 = 1, 2, 3, 4, 5

# Unpacking: Python automatically maps each value to a variable
a, b, c, d, e = T1

print(a, b, c, d, e)   # Output: 1 2 3 4 5

x,y,*z=T1           #we have put asterrisk to put remaing value in z
print(x,y,z)

print(T1.index(2))