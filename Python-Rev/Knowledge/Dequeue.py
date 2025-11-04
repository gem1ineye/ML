# -----------------------------------------
# deque (Double-Ended Queue)
# -----------------------------------------
# A deque allows insertion and removal from both ends efficiently.
# It can act as both:
# ✅ Stack (LIFO)
# ✅ Queue (FIFO)
# It’s faster than lists for append/pop operations from the left side.

from collections import deque as de

# -----------------------------------------
# Initialize a deque from a list
# -----------------------------------------
d = [1, 2, 3, 4, 5, 6]
q = de(d)
print("Initial deque:", q)

# -----------------------------------------
# Append elements (like a queue or stack)
# -----------------------------------------
q.append(99)          # Adds to the right end
print("After append(99):", q)

q.appendleft(89)      # Adds to the left end
print("After appendleft(89):", q)

# -----------------------------------------
# Remove elements
# -----------------------------------------
q.pop()               # Removes from the right end (like a stack)
print("After pop():", q)

q.popleft()           # Removes from the left end (like a queue)
print("After popleft():", q)

# -----------------------------------------
# Extend the deque
# -----------------------------------------
q.extend([44, 55, 66])  # Adds multiple elements to the right end
print("After extend([44,55,66]):", q)

# -----------------------------------------
# Rotate elements
# -----------------------------------------
# rotate(n) moves elements to the right by n steps
# rotate(-n) moves elements to the left by n steps
q.rotate(2)
print("After rotate(2):", q)
