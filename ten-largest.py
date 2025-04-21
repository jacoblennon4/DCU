#!/usr/bin/env python3

largest = int(input())
i = 0

while i < 9:
   n = int(input())
   if n > largest:
      largest = n
   i = i + 1

print(largest)
