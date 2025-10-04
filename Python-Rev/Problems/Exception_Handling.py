class InvalidAgeError(Exception):
    def __init__(self, message):
        super().__init__(message)   # pass message to base Exception
def validate_age(age):
    if 18 <= age <= 60:
        return True
    else:
        raise InvalidAgeError("Age should be kamlayak")

age=19

try:
    validate_age(age)
    print('You can join work')
except InvalidAgeError as e:
    print(e)
    
#Account Withdrawal

class InsufficientBalErr(Exception):
    pass


def withdraw(bal,amt):
    if(amt>bal):
        raise InsufficientBalErr('amount bounce')
    else:
        amt=-bal


try:
    withdraw(500,2000)
    print('Success')
except InsufficientBalErr as e:
    print(e)
    