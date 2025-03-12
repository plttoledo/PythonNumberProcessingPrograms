# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the
# decimal point.
# User input 2 numbers, print the quotient of the two numbers with a decimal point.

user_input1 = float(input("Input the first number: "))
user_input2 = float(input("Input the second number: "))

user_quotient = user_input1 / user_input2
print(f"{user_input1} divide by {user_input2} results to {user_quotient}.")