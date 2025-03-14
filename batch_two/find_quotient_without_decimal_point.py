# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
# Get user input 2 numbers, print the quotient without decimal point (use int)]

user_input1 = int(input("Enter first number: "))
user_input2 = int(input("Enter second number: "))

no_decpoint = user_input1 // user_input2
print(f"The result of the quotient without decimal point is {no_decpoint}")
