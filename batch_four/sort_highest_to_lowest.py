# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid.
# Display the number from highest to lowest. Clue: sort() function
# while True to continue asking, except ValueError once input is invalid. Print highest to lowest number using sort().

numbers = []

while True:
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)

    except ValueError:
        print("Invalid input. Exiting...")
        break

numbers.sort(reverse=True)
print(numbers)