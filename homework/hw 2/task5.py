import random 

nums = [random.randint(1, 50) for _ in range(100)]

user_num = int(input("Enter a number between 1 and 50: "))

count = nums.count(user_num)

print("The number", user_num, "appears", count, "times in the list")