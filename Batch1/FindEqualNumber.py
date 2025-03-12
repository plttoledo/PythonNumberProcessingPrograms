# Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
# User input 2 numbers, printt equal when the numbers are same.

user_input1 = float(input("Input the first number: "))
user_input2 = float(input("Input the second number: "))

if user_input1 == user_input2:
    print(f"The two numbers are equal.")
else:
    print(f"The two numbers are not equal.")