import re

# re.match(pattern, string)
# Tries to match the pattern **only at the beginning** of the string.

print(re.match('abc', 'abchfg'))  
# Output: <re.Match object; span=(0, 3), match='abc'>
# ✅ Because 'abc' is found at the start of "abchfg"

# re.fullmatch(pattern, string)
# Checks if the entire string matches the pattern
print(re.fullmatch('python', 'pythonr'))  
# Output: None (because "pythonr" ≠ "python")


# re.search(pattern, string)
# Searches for the first occurrence of the pattern anywhere in the string
print(re.search('very', 'Python is very easy'))
# Output: <re.Match object; span=(10, 14), match='very'>


# .span() -> returns the (start, end) index of the match
print(re.search('very', 'Python is very easy').span())  
# Output: (10, 14) → "very" starts at index 10 and ends at 14


print(re.findall('can', 'can you can a can as a canner'))
# Output: ['can', 'can', 'can', 'can']
# ✅ It finds 4 exact "can" substrings in the sentence
# Note: "canner" is not included because it’s not an exact "can"


# ( ... ) → Capturing group
# re.search finds the first match anywhere in the string
print(re.search('(ab)', 'ababaftbababa'))
# Output: <re.Match object; span=(0, 2), match='ab'>
# ✅ First "ab" occurs at position 0–2


# [ab]+ → character class [ab] means "either a or b"
# + means "1 or more repetitions"
# So this matches sequences of only 'a' and 'b'
print(re.findall('[ab]+', 'ababaftbababa'))
# Output: ['ababa', 'bababa']
# ✅ Finds two continuous blocks of 'a' and 'b'


# [eimt]{4} → exactly 4 characters long, 
# each character must be from the set {e, i, m, t}
print(re.search('[eimt]{4}', 'tttp '))
# Output: <re.Match object; span=(0, 4), match='tttp'>
# ✅ First 4 characters are "tttp", all valid since 't' and 'p'?? 
# ⚠️ Actually 'p' is NOT in [eimt], so result is None