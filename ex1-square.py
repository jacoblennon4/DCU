#!/usr/bin/env python3

n = int(input())
half = n // 2
i = 0
print("*" * n)

while i < half - 1:
   print("*" + " " * (n - 2) + "*")
   i = i + 1
print("*" + " " * (half - 1) + "*" + " " * (half - 1) + "*")
i = 0
while i < half - 1:
   print("*" + " " * (n - 2) + "*")
   i = i + 1
print("*" * n)
