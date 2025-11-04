from collections import Counter

invemtory=Counter(apple=50,orange=90)

def update(order):
    invemtory.subtract(order)

order=Counter(apple=20,orange=76)
update(order)

print(invemtory)