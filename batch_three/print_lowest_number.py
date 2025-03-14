# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the lowest number

lowest = None

while True:
    try:
        num = int(input("Enter a number: "))
        if lowest is None or num < lowest:
            lowest = num

    except ValueError:
        print("Invalid input. Exiting...")
        break

if lowest is not None:
    print(f"The lowest number entered was {lowest}")
else:
    print("There were no valid numbers entered.")