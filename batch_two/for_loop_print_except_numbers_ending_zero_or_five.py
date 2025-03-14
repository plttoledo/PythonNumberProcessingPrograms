# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
# Loop print all numbers from 0 to 100 except numbers ending in 0 or 5

for num in range(101):
    if num % 10 != 0 and num % 5 != 0:
        print(num)

