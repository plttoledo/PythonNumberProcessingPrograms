# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
# User input 2 numbers, print the numbers in between the inputs

user_input1 = int(input("Enter first number: "))
user_input2 = int(input("Enter second number: "))

if user_input1 < user_input2:
    print("The first input should be bigger than the second input.")
else:
    for num in range(user_input2 + 1, user_input1):
        print(num)