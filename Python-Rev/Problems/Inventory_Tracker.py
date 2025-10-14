from collections import UserDict

# -----------------------------------------
# Custom Inventory Tracker (inherits from UserDict)
# -----------------------------------------
# UserDict allows you to create customized dictionary behavior by subclassing.

class Inventory_Tracker(UserDict):
    def __init__(self):
        # Initialize the parent UserDict (sets up internal 'data' dictionary)
        super().__init__()
    
    def __setitem__(self, item, qty):
        """
        ✅ Overriding the default assignment operator (=).
        Ensures:
          - Product name (key) must be a string.
          - Quantity (value) must be an integer.
          - Keys are stored in lowercase (case-insensitive tracking).
        """
        if not isinstance(item, str) or not isinstance(qty, int):
            raise Exception('Product and quantity should be of type string: integer')
        
        super().__setitem__(item.lower(), qty)   # Store all keys in lowercase
        
    def __getitem__(self, item):
        """
        ✅ Retrieves the item quantity (case-insensitive).
        """
        return super().__getitem__(item.lower())
    
    def __delitem__(self, item):
        """
        ✅ Deletes an item from inventory (case-insensitive).
        """
        return super().__delitem__(item.lower())
    
    def __contains__(self, item):
        """
        ✅ Checks if an item exists in inventory (case-insensitive).
        """
        return super().__contains__(item.lower())
    
    def update_stock(self, item, qty):
        """
        ✅ Updates stock quantity for an item.
        If item exists → adds (or subtracts) qty.
        If not → creates new entry.
        """
        if item in self:
            self[item] += qty
        else:
            self[item] = qty


# -----------------------------------------
# Object Creation and Testing
# -----------------------------------------
ity = Inventory_Tracker()

# Add products to inventory
ity['Apple'] = 10
ity['banana'] = 20

# Accessing items (case-insensitive)
print(ity['Apple'])     # Output: 10

# Update existing stock
ity.update_stock('Apple', -1)
print(ity['Apple'])     # Output: 9
