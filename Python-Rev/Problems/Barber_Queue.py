from collections import deque

customers=deque()

def walk_in(customer):
    customers.append(customer)

def serviced():
    cust=customers.popleft()
    print(cust,'Has been serviced')


walk_in('Manan')
walk_in('Akash')
walk_in('Mohan')
serviced()
serviced()

print(customers)