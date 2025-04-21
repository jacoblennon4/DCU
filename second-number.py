#!/usr/bin/env python3

s = input()
i = 0
count = 0   # count of numbers found

while i < len(s):
    if "0" <= s[i] <= "9":   # Found a digit, beginning of a number
        start = i  # remember the start of the number
        while i < len(s) and "0" <= s[i] <= "9":   # get the full number
            i = i + 1
        count = count + 1
        if count == 2:   # If it's the second number, print it
            print(s[start:i], start)  # number and its position
    i = i + 1
