# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
# Loop program that prints all numbers from 0 to 100 except numbers that ends in zero.

for num in range(101):
    if num % 10 != 0:
        print(num)