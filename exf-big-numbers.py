#!/usr/bin/env python3

i = 0
big = 0
neg = 0
while i < 10:
   n = int(input())
   if n >= 100:
      big = big + 1
   elif n <= -100:
      neg = neg + 1
   total = neg + big
   i = i + 1
print(total)
