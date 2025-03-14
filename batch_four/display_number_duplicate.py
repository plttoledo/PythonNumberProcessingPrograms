# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

numbers = []
entries = []

for i in range(10):
    num = int(input(f"Enter #{i+1}: "))
    numbers.append(num)

for num in numbers:
    if numbers.count(num) != 1 and num not in entries:
        print(num)
        entries.append(num)