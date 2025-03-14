# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the average.
# while True to continue asking, except ValueError once input is invalid. Get average.

numbers = []

while True:
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)

        average = sum(numbers)/len(numbers)

    except ValueError:
        print("Invalid input. Exiting...")
        print(average)
        break