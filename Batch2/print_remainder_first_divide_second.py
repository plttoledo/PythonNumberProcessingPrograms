# Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.
# Get user input 2 numbers, print the remainder of the first number divided by the second number (use int and modulo)

user_input1 = int(input("Enter first number: "))
user_input2 = int(input("Enter second number: "))

get_modulo = user_input1 % user_input2
print(f"The remainder of the first number ({user_input1}) divided by the second number({user_input2}) is {get_modulo}")