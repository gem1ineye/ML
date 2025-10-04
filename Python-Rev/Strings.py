# String for slicing operations
s1 = "Hello World"

# -------------------------------
# SLICING IN PYTHON: s1[start:stop:step]
# -------------------------------

print(s1[::2])       # Takes every 2nd character → "HloWrd"
print(s1[:5])        # From start to index 4 (not including 5) → "Hello"
print(s1[::-1])      # Reverses the string → "dlroW olleH"

# -------------------------------
# 'in' OPERATOR - checks if a substring exists
# -------------------------------
print('ol' in s1)    # False → substring 'ol' not found together in "Hello World"
print('o' in s1)     # True  → character 'o' is present

# -------------------------------
# STRING COMPARISON - Lexicographical order (dictionary-like)
# -------------------------------
print('apply' > 'apple')   # True  → 'y' comes after 'e'
print('data' > 'Data')     # True  → lowercase letters are considered greater
print('2nd' > 'd')         # False → numbers come before letters

# -------------------------------
# FINDING SUBSTRINGS
# -------------------------------
z1 = "How are You"
# find(substring, start_index, end_index)
# searches for 'are' starting from index 4 till end of string
print(z1.find('are', 4, len(z1)))  # Output: -1 (not found because 'are' starts at index 4)

# -------------------------------
# COUNTING OCCURRENCES
# -------------------------------
z2 = "It's always me only me"
print(z2.count('me'))  # Counts how many times 'me' appears → 2

# -------------------------------
# STRING ALIGNMENT AND FILLING
# -------------------------------
z1 = "heloo"

# Left justify with 'u' to make total width 11 → "heloouuuuuu"
w2 = z1.ljust(11, 'u')
print(w2)

# Right justify with '*' to width 9 → "****heloo"
print(z1.rjust(9, '*'))

# Center justify with '*' to width 9 → "***heloo*"
print(z1.center(9, '*'))

# zfill fills with zeroes to width 9 → "0000heloo"
print(z1.zfill(9))

# str.lstrip(chars) removes all characters present in 'chars' 
# from the **start** (left side) of the string 
# until it finds a character that is not in 'chars'.

# Example 1: Removing leading spaces
string = "         Hello"
print(string)                 # Original string with spaces
print(string.lstrip('e'))     # No 'e' at the start, so spaces remain removed by default

# Example 2: Removing leading 'e's
s = "eeexample"
print(s.lstrip('e'))          # Removes all 'e's from the start -> "xample"

# Example 3: Using strip() to remove specific characters 
# from BOTH ends (left and right) of the string
s = '#! Heelo  $ ('
print(s.strip('#!  $ ('))     # Removes '#!  $ (' from both ends -> "Heelo"

print(s.strip('#!  $ ('))


# -----------------------------
# String Find and Replace Examples
# -----------------------------

s3 = "Hello ** World"

# replace(old, new, count)
# Replaces the first occurrence (count=1) of '*' with a space
print(s3.replace('*', ' ', 1))   # Output: "Hello  * World"


# join(iterable)
# Inserts the string (here j1) between every character of the iterable (here j2)
j1 = '/-'
j2 = "gama"
print(j1.join(j2))               # Output: "g/-a/-m/-a"


# split(separator)
# Splits the string wherever the separator occurs.
# If no separator is provided, it splits by spaces.
j3 = '''why are-you
here'''
print(j3.split('-'))             # Splits by '-' -> ['why are', 'you\nhere']


# splitlines()
# Splits the string into a list where each line is a separate element
print(j3.splitlines())           # Output: ['why are-you', 'here']




# -----------------------------
# String Checking and Partitioning Examples
# -----------------------------

j3 = '''why are-you
here'''

# startswith(prefix, start=0, end=len(string))
# Checks if the string starts with the given prefix
print(j3.startswith('hy'))   # False -> because it starts with 'w' not 'hy'

# endswith(suffix, start=0, end=len(string))
# Checks if the string ends with the given suffix
print(j3.endswith('ere'))    # True -> because it ends with 'ere'


# -----------------------------
# Removing Prefix and Suffix
# -----------------------------
j3 = "Python is very easy"

# removeprefix(prefix)
# Removes the prefix from the string if it exists
print(j3.removeprefix('Py'))   # Output: "thon is very easy"

# removesuffix(suffix)
# Removes the suffix from the string if it exists
print(j3.removesuffix('asy'))  # Output: "Python is very e"


# -----------------------------
# Partitioning Strings
# -----------------------------
# partition(separator)
# Splits the string into a tuple: (before_separator, separator, after_separator)
print(j3.partition(' '))       # Output: ('Python', ' ', 'is very easy')

# rpartition(separator)
# Similar to partition, but splits at the last occurrence of the separator
print(j3.rpartition('s'))      # Output: ('Python is very ea', 's', 'y')
# -----------------------------
# String Case Conversion Methods
# -----------------------------

# Converts entire string to UPPERCASE
print(j3.upper())        # Example: "Python is very easy" -> "PYTHON IS VERY EASY"

# Converts entire string to lowercase
print(j3.lower())        # Example: "Python is very easy" -> "python is very easy"

# Capitalizes only the first character, rest becomes lowercase
print(j3.capitalize())   # Example: "Python is very easy" -> "Python is very easy"

# Converts the first character of each word to uppercase (Title Case)
print(j3.title())        # Example: "Python is very easy" -> "Python Is Very Easy"

# Swaps case: lowercase -> uppercase and uppercase -> lowercase
print(j3.swapcase())     # Example: "Python is very easy" -> "pYTHON IS VERY EASY"


# -------------------------------
# CHECK IF STRING IS ALPHABETIC
# -------------------------------
j3 = 1234
# print(j3.isalpha())  # ❌ ERROR: integers don't have string methods

j3 = "hellohoeareyo"
print(j3.isalpha())  
# ✅ True because the string contains only alphabetic characters (a-z, A-Z)

# -------------------------------
# CHECK IF STRING IS NUMERIC
# -------------------------------
j3 = "1234"
print(j3.isnumeric())  
# ✅ True because the string consists only of numeric digits

# -------------------------------
# CHECK FOR WHITESPACE CHARACTERS
# -------------------------------
j3 = "\n \v \r \f   "
print(j3.isspace())  
# ✅ True because the string only has whitespace characters (newlines, vertical tabs, carriage returns, etc.)

# -------------------------------
# CHECK IF STRING IS PRINTABLE
# -------------------------------
print(j3.isprintable())  
# ❌ False because escape sequences like '\n', '\v', '\r', '\f' are NOT considered printable characters

s = '125'
print(s.isdecimal())      # True (all digits between 0–9)

s = '1.25'
print(s.isdecimal())      # False (decimal point is not a digit)


s = '1682'
print(s.isdigit())        # True

s = '²'  # Superscript 2
print(s.isdigit())        # True (special numeric characters count as digits)


s = '5½'   # 5 and 1/2
print(s.isnumeric())      # True (fraction recognized as numeric)

s = 'Ⅴ'    # Roman numeral five
print(s.isnumeric())      # True

s = '1.5'
print(s.isnumeric())      # False (decimal point not numeric)


# -----------------------------
# String Formatting (f-strings)
# -----------------------------
x = 567
y = 'gabriel'

# f-strings (introduced in Python 3.6) allow embedding variables directly in strings
print(f'{y} is {x}th times older then Alisia')
# Output: gabriel is 567th times older then Alisia
