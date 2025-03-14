# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input
# when the inputted number have duplicate.

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)

        if numbers.count(num) > 1:
            print(f"{num} is duplicated.")
        else:
            print(f"{num} is unique.")

    except ValueError:
        print("Invalid input. Exiting...")
        break