# -----------------------------
# Properties of Sets
# -----------------------------
# ✅ Mutable (can add/remove elements)
# ✅ No duplicates allowed
# ✅ Can hold heterogeneous elements (int, str, bool, etc.)
# ❌ No indexing / slicing (because sets are unordered)
# ✅ Unordered collection (order is not guaranteed)

# Creating a set directly
s1 = {1, 23, 4, 5, 8}
print(s1)    # e.g., {1, 4, 5, 8, 23}  (order may differ)


# Creating a set from a string → unique characters only
s2 = set('Python')
print(s2)    # e.g., {'y', 'n', 'h', 't', 'o', 'P'}


# Creating a set from a list with mixed data types
s3 = set([1, 'abc', True, 'a', 'a'])
print(s3)    # Note: 1 and True are treated as the same → duplicates removed


# ⚠️ Special Note:
# {} creates an empty DICTIONARY, not a set
s4 = {}      
print(type(s4))   # <class 'dict'>

# To create an empty set → use set()
s5 = set()
print(type(s5))   # <class 'set'>

# Or initialize with one element
s6 = {3}
print(s6)         # {3}



# -----------------------------
# Set Operations in Python
# -----------------------------

set1 = {1, 2, 3, 5, 7}
set2 = {6, 7, 8, 9, 2}

# union() → combines all unique elements from both sets
print(set1.union(set2))        
# Output: {1, 2, 3, 5, 6, 7, 8, 9}


# intersection() → common elements in both sets
print(set1.intersection(set2)) 
# Output: {2, 7}


# difference() → elements in set1 but NOT in set2
print(set1.difference(set2))   
# Output: {1, 3, 5}


#Adding and Deleting :(add delete copy pop update)
set1.add(99)
print(set1)

