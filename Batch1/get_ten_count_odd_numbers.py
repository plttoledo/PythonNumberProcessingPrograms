# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
# User input 10 numbers, print how many odd numbers.

odd_num = 0
for i in range(10):
    num = float(input(f"Input #{i+1}: "))
    if num % 2 != 0:
        odd_num += 1

print(f"There are {odd_num} odd numbers.")