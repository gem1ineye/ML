import os
import time

# -----------------------------------------
# File and Directory Path Checks
# -----------------------------------------

# Checks whether the given path exists (file or folder)
print(os.path.exists('/Users/gem1ineye/Documents/Technical Stuff/Python/ML/Python-Rev/Knowledge/data.txt'))
# ✅ True → Path exists
# ❌ False → File or folder not found

# Checks whether the given path points to a file
print(os.path.isfile('/Users/gem1ineye/Documents/Technical Stuff/Python/ML/Python-Rev/Knowledge/data.txt'))
# Returns True if it's a file, False otherwise

# Checks whether the given path points to a directory
print(os.path.isdir('/Users/gem1ineye/Documents/Technical Stuff/Python/ML/Python-Rev/Knowledge/data.txt'))
# False — since it's a file

print(os.path.isdir('/Users/gem1ineye/Documents/Technical Stuff/Python/ML/Python-Rev/Knowledge/'))
# True — since it's a folder

# -----------------------------------------
# Path Splitting and Joining
# -----------------------------------------

# Splits the path into (directory, filename)
print(os.path.split('/Users/gem1ineye/Documents/Technical Stuff/Python/ML/Python-Rev/Knowledge/data.txt'))
# Output: ('/Users/.../Knowledge', 'data.txt')

# Joins two paths properly according to the OS
print(os.path.join('/Users/gem1ineye/Documents/Technical Stuff/Python/ML/Python-Rev/Knowledge', 'data.txt'))
# Output: '/Users/.../Knowledge/data.txt'

# Extracts only the filename from a path
print(os.path.basename('/Users/gem1ineye/Documents/Technical Stuff/Python/ML/Python-Rev/Knowledge/data.txt'))
# Output: 'data.txt'

# Extracts only the directory name from a path
print(os.path.dirname('/Users/gem1ineye/Documents/Technical Stuff/Python/ML/Python-Rev/Knowledge/data.txt'))
# Output: '/Users/.../Knowledge'

# -----------------------------------------
# File Timestamps (Access, Modification, Creation)
# -----------------------------------------
# os.path.getatime() → Last access time
# os.path.getmtime() → Last modification time
# os.path.getctime() → Creation time (on Windows) / metadata change (on Unix)

print(time.ctime(os.path.getatime('/Users/gem1ineye/Documents/Technical Stuff/Python/ML/Python-Rev/Knowledge/data.txt')))
# Converts the last access timestamp into human-readable format

print(time.ctime(os.path.getmtime('/Users/gem1ineye/Documents/Technical Stuff/Python/ML/Python-Rev/Knowledge/data.txt')))
# Converts the last modification timestamp

print(time.ctime(os.path.getctime('/Users/gem1ineye/Documents/Technical Stuff/Python/ML/Python-Rev/Knowledge/data.txt')))
# Converts creation time (or metadata change time in macOS/Linux)
