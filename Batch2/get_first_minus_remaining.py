# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
# Get user input 10 numbers, print result of first number minus the rest

numbers = []

for i in range(10):
    num = float(input(f"Enter #{i+1}: "))
    numbers.append(num)

result = numbers[0] - sum(numbers[1:])
print(f"{result} is the result of the first number minus the remaining numbers.")