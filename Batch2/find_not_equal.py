# Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
# Get user input two numbers, print not equal numbers are not the same

user_input1 = float(input("Enter first number: "))
user_input2 = float(input("Enter second number: "))

if user_input1 != user_input2:
    print("The numbers are not equal")
else:
    print("The numbers are equal")