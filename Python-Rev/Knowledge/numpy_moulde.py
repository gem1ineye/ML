import numpy as np   # Import NumPy (numerical computing library)

# -----------------------------------------
# 1D Array (Vector)
# -----------------------------------------
# A 1-dimensional NumPy array → acts like a list but supports mathematical operations
arr = np.array([1, 2, 3, 5, 6, 89])
print(arr)
# Output: [ 1  2  3  5  6 89]

# -----------------------------------------
# 2D Array (Matrix)
# -----------------------------------------
# A 2-dimensional array (list of lists) → represents rows and columns
arr2 = np.array([[1, 2], [3, 4]])
print(arr2)
# Output:
# [[1 2]
#  [3 4]]

# -----------------------------------------
# 3D Array (Tensor)
# -----------------------------------------
# A 3-dimensional array → can represent multiple 2D matrices (useful for deep learning)
arr3 = np.array([
    [[1, 2], [3, 4]],    # First 2x2 matrix
    [[6, 7], [9, 8]]     # Second 2x2 matrix
])
print(arr3)
# Output:
# [[[1 2]
#   [3 4]]
#  [[6 7]
#   [9 8]]]

# -----------------------------------------
# Checking Number of Dimensions
# -----------------------------------------
print(arr.ndim)   # Output: 1  → 1D array
print(arr2.ndim)  # Output: 2  → 2D array


# NumPy Array Creation Functions
# -----------------------------------------
# Topic: np.linspace(), np.zeros(), np.empty(), np.eye(), np.diag(), np.arange()
# -----------------------------------------

# 1️⃣ np.linspace(start, stop, num)
# Creates an array with 'num' evenly spaced values between 'start' and 'stop' (inclusive)
arr1 = np.linspace(0, 10, 5)     # 5 values from 0 → 10 (inclusive)
print("np.linspace(0, 10, 5):", arr1)
# Output: [ 0.   2.5  5.   7.5 10. ]

# 2️⃣ np.zeros(shape)
# Creates an array filled with zeros. Useful for initialization.
arr2 = np.zeros((2, 3))          # 2x3 matrix of zeros
print("\nnp.zeros((2, 3)):\n", arr2)
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]]

# 3️⃣ np.empty(shape)
# Creates an array without initializing entries (contains random garbage values in memory)
arr3 = np.empty((2, 2))          # 2x2 matrix (values depend on memory state)
print("\nnp.empty((2, 2)):\n", arr3)
# Output (random): [[1.23e-322 0.00e+000]
#                   [0.00e+000 0.00e+000]]

# 4️⃣ np.eye(N)
# Creates an identity matrix (square matrix with 1s on the main diagonal)
arr4 = np.eye(3)                 # 3x3 identity matrix
print("\nnp.eye(3):\n", arr4)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 5️⃣ np.diag(v)
# Creates a diagonal matrix from a list or extracts the diagonal from a matrix
arr5 = np.diag([10, 20, 30])     # Create diagonal matrix with 10, 20, 30 on main diagonal
print("\nnp.diag([10, 20, 30]):\n", arr5)
# Output:
# [[10  0  0]
#  [ 0 20  0]
#  [ 0  0 30]]

# Extract diagonal from the created matrix
print("\nDiagonal elements:", np.diag(arr5))
# Output: [10 20 30]

# 6️⃣ np.arange(start, stop, step)
# Creates an array with values from 'start' to 'stop' (exclusive), with a given 'step'
arr6 = np.arange(0, 10, 2)       # Values: 0, 2, 4, 6, 8
print("\nnp.arange(0, 10, 2):", arr6)
# Output: [0 2 4 6 8]