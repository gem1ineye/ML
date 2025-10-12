# -----------------------------
# Using Enum for Order Status
# -----------------------------

from enum import Enum   # Importing Enum base class

# Enum class to define possible order statuses
class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5


# Class representing an Order
class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.status = OrderStatus.PENDING     # Default status is PENDING
    
    def update_status(self, new_status):
        """
        Updates the order status.
        Only accepts valid Enum members (OrderStatus).
        """
        if isinstance(new_status, OrderStatus):        # ensures valid Enum value
            self.status = new_status
            print(f"Order {self.order_id} updated to {self.status.name}")
        else:
            print("Invalid status! Must be a member of OrderStatus Enum.")
    
    def display(self):
        """Displays current order details"""
        print("Order ID:", self.order_id)
        print("Customer:", self.customer_name)
        print("Status:", self.status.name)   # .name gives Enum label


# -----------------------------
# Object Creation and Usage
# -----------------------------
order1 = Order(1002, 'Adamk')          # creates order with default status = PENDING
order1.display()                       # shows order details

order1.update_status(OrderStatus.SHIPPED)   # updates status to SHIPPED
order1.display()                       # displays updated order info
