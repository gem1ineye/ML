from collections import Counter

# Item prices
Price = Counter(Soap=50, Brush=70, Shampoo=200, Food=700)

def generate_bill(order):
    total = 0
    print("Item\tPrice\tQty\tSubtotal")
    print("-" * 40)
    for item in order.keys():
        subtotal = order[item] * Price[item]
        print(f"{item}\t{Price[item]}\t{order[item]}\t{subtotal}")
        total += subtotal
    print("-" * 40)
    print("Total Amount:", total)

# Example order
Order = Counter(Soap=5, Brush=3)
generate_bill(Order)
