from collections import Counter
import re

s = "This is very nice cafe in kota \n as well as this is also going to be fun for us"

# Split using regex for space, newline, or tab
words = re.split(r'[\s\n]+', s.strip())

# Count frequency of each word
count = Counter(words)
print(count)
