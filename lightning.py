#!/usr/bin/env python3

n = int(input())

i = 0
while i < n - 1:
   print((n - i - 1) * " " + "*")
   i = i + 1

print(n * "*")

i = 0
while i < n - 1:
   print((n - i - 2) * " " + "*")
   i = i + 1
