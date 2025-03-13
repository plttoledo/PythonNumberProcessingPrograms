# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
# Get user input 2 numbers, print the smaller number

user_input1 = float(input("Enter first number: "))
user_input2 = float(input("Enter second number: "))

if user_input1 < user_input2:
    print(f"{user_input1} is the smaller number")
else:
    print(f"{user_input2} is the smaller number")