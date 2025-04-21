#!/usr/bin/env python3

# Step 1: Create an empty list to store the numbers
numbers = []

# Step 2: Read numbers until 0 is encountered and add them to the list
num = int(input())
while num != 0:
    numbers.append(num)
    num = int(input())

# Step 3: Reverse the list
numbers.reverse()

# Step 4: Print each number from the reversed list
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
