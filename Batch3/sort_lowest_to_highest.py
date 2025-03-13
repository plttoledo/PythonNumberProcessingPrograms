# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the number from lowest to highest. Clue: sort() function

numbers = []

while True:
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)

    except ValueError:
        print("Invalid input. Exiting...")
        break

numbers.sort()
print(numbers)