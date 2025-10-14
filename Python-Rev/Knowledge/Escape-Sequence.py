print("I\'m Harshit")     # Single quote

print('valid\lso')

print('\x41')         #2 digit hexa

print('\u0041')      #4digit hexa

print('\U00000041')  #8digit hexa# -----------------------------
# Escape Sequences and Unicode in Strings
# -----------------------------

# Using backslash (\) to escape a single quote inside a string
print("I\'m Harshit")      # Output: I'm Harshit


# Invalid escape sequence (\l). Python may warn about it.
# If you mean a normal backslash + l, use '\\l'
print('valid\\lso')        # Output: valid\lso


# Hexadecimal escape sequence (\xNN) → 2-digit hex
# \x41 corresponds to ASCII code 65, which is 'A'
print('\x41')              # Output: A


# Unicode escape sequence (\uNNNN) → 4-digit hex
# \u0041 also represents 'A'
print('\u0041')            # Output: A


# Unicode escape sequence (\UNNNNNNNN) → 8-digit hex
# \U00000041 also represents 'A'
print('\U00000041')        # Output: A


# -----------------------------
# print() with sep and end parameters
# -----------------------------

# sep = defines what goes between values
# end = defines what comes at the end of the print instead of newline
print('hi', 67, True, sep='-', end='\t')   # Output: hi-67-True   (and adds a tab instead of newline)
print('hi')                                # Continues on the same line due to end='\t'


# -----------------------------
# String Formatting (Old style with % operator)
# -----------------------------
item = 'Memory'
size = 32
price = 56

# %d = integer, %s = string, %f = float
print('Cost of %dGB %s is $%f' % (size, item, price))
# Output: Cost of 32GB Memory is $56.000000
