# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
# User input 10 numbers, print the sum of all the numbers.
total = 0
for i in range(10):
    num = float(input(f"Input #{i+1}: "))
    total += num

print(f"The sum of the 10 numbers is {total}.")
