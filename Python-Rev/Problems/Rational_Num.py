# -----------------------------------------
# Operator Overloading with Rational Numbers
# -----------------------------------------
# This class defines arithmetic and comparison operations
# for fractions (numerator/denominator format).

class Rational:
    def __init__(self, num, den):
        # Initialize numerator and denominator
        self.num = num
        self.den = den
    
    def __add__(self, other):
        """
        ✅ Overload '+' operator for adding two Rational numbers.
        Formula:
            (a/b) + (c/d) = (ad + bc) / bd
        """
        num = (self.num * other.den) + (self.den * other.num)
        den = (self.den * other.den)
        return Rational(num, den)   # Return new Rational object
    
    def __mul__(self, other):
        """
        ✅ Overload '*' operator for multiplying two Rational numbers.
        Formula:
            (a/b) * (c/d) = (ac) / (bd)
        """
        return Rational(self.num * other.num, self.den * other.den)
    
    def __lt__(self, other):
        """
        ✅ Overload '<' operator for comparison.
        Formula:
            (a/b) < (c/d) if ad < bc
        """
        return self.num * other.den < self.den * other.num
    
    def __str__(self):
        """
        ✅ String representation for easy printing.
        """
        return '(' + str(self.num) + ', ' + str(self.den) + ')'


# -----------------------------------------
# Object Creation and Testing
# -----------------------------------------
r1 = Rational(1, 2)
r2 = Rational(2, 3)

# '+' calls __add__()
r3 = r1 + r2

# '*' calls __mul__()
r4 = r1 * r2

# '<' calls __lt__()
print(r1 < r2)   # True → (1/2) < (2/3)

# Printing the results (calls __str__())
print(r3)        # (7, 6)  → (1/2 + 2/3 = 7/6)
print(r4)        # (2, 6)  → (1/2 * 2/3 = 2/6)
