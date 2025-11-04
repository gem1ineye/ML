import heapq as hq

# -----------------------------------------
# Python: heapq (Heap Queue / Priority Queue)
# -----------------------------------------
# A heap is a binary tree where:
# ✅ Each parent node ≤ its children (Min-Heap)
# ✅ The smallest element is always at index 0
# ✅ Very efficient for priority queue operations (O(log n))

# -----------------------------------------
# Step 1: Create a list
# -----------------------------------------
h = [10, 45, 20, 15, 7, 98, 1]

# -----------------------------------------
# Step 2: Convert the list into a heap
# -----------------------------------------
hq.heapify(h)
# Rearranges elements in-place to satisfy the heap property
print("Initial heap:", h)
# Smallest element (1) will now be at the root (index 0)

# -----------------------------------------
# Step 3: Push new element into heap
# -----------------------------------------
hq.heappush(h, 33)
# Automatically adjusts heap to maintain order
print("After pushing 33:", h)

# -----------------------------------------
# Step 4: Pop the smallest element
# -----------------------------------------
smallest = hq.heappop(h)
# Removes and returns the smallest element (root)
print("After popping smallest element:", h)
print("Popped element:", smallest)

# -----------------------------------------
# Step 5: Get N largest and smallest elements (without modifying heap)
# -----------------------------------------
print("2 largest elements:", hq.nlargest(2, h))
print("2 smallest elements:", hq.nsmallest(2, h))
