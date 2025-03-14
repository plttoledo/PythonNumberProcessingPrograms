# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the highest number
# while True to continue asking, except ValueError once input is invalid. Print highest number, similar to batch 3, program 4.

highest = None

while True:
    try:
        num = int(input("Enter a number: "))
        if highest is None or num > highest:
            highest = num

    except ValueError:
        print("Invalid input. Exiting...")
        break

if highest is not None:
    print(f"The highest number entered was {highest}")
else:
    print("There were no valid numbers entered.")