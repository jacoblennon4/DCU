#!/usr/bin/env python3

n = int(input())

i = 0
while i < n:
   print(" " * i + "*" + " " * (n - 2 * i - 2) + "*")
   i = i + 1
