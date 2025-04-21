#!/usr/bin/env python3

n = int(input())

i = 1

while i < n:
    if i == 1:
        print("*")
    elif i == n:
        print("*" * n)
    else:
        print("*" + " " * (i - 2) + "*")
    i += 1
print("*" * n)
