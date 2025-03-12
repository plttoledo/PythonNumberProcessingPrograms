# Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is
# raised to the second number.
# User input 2 numbers, print the result of the first number raised to the second number.

user_input1 = float(input("Input the first number: "))
user_input2 = float(input("Input the second number: "))

raised_number = user_input1 ** user_input2
print(f"{user_input1} raised to {user_input2} results to {raised_number}.")