#!/usr/bin/env python3

# Start by reading the first input
s = input()

# Loop until we encounter "end"
while s != "end":
    n = int(s)  # Convert the input string to an integer

    # Check if n is divisible by 3 or 5, but not both
    if (n % 3 == 0) ^ (n % 5 == 0):
        print(n)  # Print the number if it meets the criteria

    # Read the next input
    s = input()
