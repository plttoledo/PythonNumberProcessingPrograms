# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
# Get 10 user input numbers. Print the numbers that don't have duplicates.

numbers = []

for i in range(10):
    num = int(input(f"Enter #{i+1}: "))
    numbers.append(num)

for num in numbers:
    if numbers.count(num) == 1:
        print(num)