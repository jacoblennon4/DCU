#!/usr/bin/env python3

smallest = int(input())
i = 0

while i < 9:
   n = int(input())
   if n < smallest:
      smallest = n
   i = i + 1

print(smallest)
