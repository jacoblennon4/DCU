#!/usr/bin/env python3

n = int(input())

i = 0
a, b = 0, 1
while i < n:
   print(a)
   a, b = b, a + b
   i = i + 1
