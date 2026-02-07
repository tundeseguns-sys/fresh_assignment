# Write a program using a while loop that asks the user for a number n and calculates the sum of numbers from 1 to n.

total = 0
count = 0
n = int(input("Enter a number (n): "))
while count <= n:
    total += count
    count += 1

print(f"The sum of numbers from 1 to {n} is: {total}")


# Write a program using a while loop that asks the user for a number and calculates its factorial.

factorial = 1
count = 1
n = int(input("Enter a number to find its factorial: "))
while count <= n:
    factorial *= count
    count += 1

print(f"The factorial of {n} is: {factorial}")
