# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the number with the most number of duplicate.
# Use while True loop for asking to input a number and use try, then use except ValueError for an invalid input.

numbers = []

while True:
    try:
        num = int(input(f"Enter a number: "))
        numbers.append(num)

    except ValueError:
        print("Invalid input. Exiting...")
        break

if numbers:
    most_common = numbers[0]
    max_count = 0

    for n in numbers:
        count = numbers.count(n)
        if count > max_count:
            max_count = count
            most_common = n

    print(f"The number with the most duplicates is {most_common}, which appeared {max_count} times.")

else:
    print("There are no valid numbers.")