def unique_num(*args):
    nums = set(args)
    return list(nums)

print("Enter nums seperated by spaces :")
nums=input("")

numbers=[int(n) for n in nums.split()]
unique=unique_num(*numbers)

print(unique)