# -----------------------------
# List Basics in Python
# -----------------------------

# Creating a list with mixed data types
l1 = [1, 3.5, 9.0, True]
print(type(l1))          # <class 'list'>


# Creating a list using list() constructor
# ⚠️ list() only takes ONE iterable argument, not multiple
# l2 = list((1,2,3,4), (7,8,9))   ❌ Not allowed
l2 = list((1, 2, 4, 56))          # ✅ Tuple converted to list
print(l2)                         # [1, 2, 4, 56]


# Converting a string into a list → splits into characters
l3 = list('abcgh')
print(l3)                         # ['a', 'b', 'c', 'g', 'h']


# Updating list elements (lists are mutable)
l1[3] = False                     # Replace True with False
print(l1)                         # [1, 3.5, 9.0, False]


# append() → adds a new element at the end
l1.append(3+7j)                   # Add complex number
print(l1)                         # [1, 3.5, 9.0, False, (3+7j)]


# -----------------------------
# List Slicing
# Syntax: list[start : end : step]
# -----------------------------
# start → index to begin (inclusive)
# end   → index to stop (exclusive)
# step  → jump size (default = 1)

k1 = [2, 3, 4, 5, 6]

# Negative indexing:
# -1 → last element, -2 → second last, etc.
print(k1[-4:-2])  
# Output: [3, 4]
# ✅ Explanation:
# k1 = [2, 3, 4, 5, 6]
# Indexing:   0   1   2   3   4
# Negative:  -5  -4  -3  -2  -1
# Slice from -4 (element 3) up to -2 (element 5, excluded)


k1=[1,2,3]
k2=[3,2,1]
print(k2>k1)

k1[2:2]=[10]     #this is way of inserting element using Slicing  
print(k1)

k1[1:3]=[99]  #This is will replace two element at index 1 and 2 with 99.
print(k1)

k1.extend([44,55,66])
print(k1)

k1[len(k1):]=[45,56,67]
print(k1)


t1=[1,2,4]
t2=t1.copy()
print(t2)

t2[1]=99

print(t1)
print(t2)

# -----------------------------
# List Comprehension
# Syntax: [expression for item in iterable if condition]
# -----------------------------

e1 = [1, 2, 4, 5]

# Squaring each element in e1
e2 = [x**2 for x in e1]
print(e2)    # [1, 4, 16, 25]


# Converting each character of a string to lowercase
l2 = [x.lower() for x in 'PytHOn']
print(l2)    # ['p', 'y', 't', 'h', 'o', 'n']


# Filtering only alphabetic characters from a string
l5 = [x for x in 'salt#$ed' if x.isalpha()]
print(l5)    # ['s', 'a', 'l', 't', 'e', 'd']
