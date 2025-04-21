#!/usr/bin/env python3

n = int(input())

i = 0
print(n)
while i < 9:
   if n % 2 == 0:
      n = n // 2
   else:
      n = 3 * n + 1
   print(n)
   i = i + 1
