# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
# User input 2 numbers, print the bigger number.

user_input1 = float(input("Input the first number: "))
user_input2 = float(input("Input the second number: "))

if user_input1 > user_input2:
    print(f"{user_input1} is the bigger number")
else:
    print(f"{user_input2} is the bigger number")