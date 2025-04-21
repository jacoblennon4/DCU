#!/usr/bin/env python3

n = int(input())
i = 0

print(" " * (n - 1) + "*")
while i < n - 1:
   print(" " * (n - 1 - i - 1) + "*" + " " * (i + 1 + i) + "*")
   i = i + 1
