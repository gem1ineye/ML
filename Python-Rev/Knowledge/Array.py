import array   # Import Python's built-in array module

# -----------------------------------------
# Array Creation — Typecode 'i' (Signed Integer)
# -----------------------------------------
# Syntax: array.array(typecode, initializer)
# typecode 'i' → signed integer (usually 4 bytes)
arr = array.array('i', [10, 20, 30, 40, 50])

print("Integer Array:", arr)
# Output: array('i', [10, 20, 30, 40, 50])

# -----------------------------------------
# Byte Array Creation — Typecode 'b'
# -----------------------------------------
# Typecode 'b' → signed char (1 byte per element)
# You can initialize it with a bytes object (b'...')
s1 = b'abccdfgt'   # bytes literal
arr1 = array.array('b', s1)

print("Byte Array:", arr1)
# Output: array('b', [97, 98, 99, 99, 100, 102, 103, 116])

# -----------------------------------------
# Array Slicing
# -----------------------------------------
# Works similar to Python lists
print("Slice arr1[1:3]:", arr1[1:3])
# Output: array('b', [98, 99])
