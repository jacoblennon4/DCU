#!/usr/bin/env python3

counts = [0] * 10
s = input()

while s != "end":
   s = int(s)
   i = 0
   while i < 10:
      if s == i:
         counts[i] = counts[i] + 1
      i = i + 1
   s = input()
i = 0
while i < 10:
   print(i, "*" * counts[i])
   i = i + 1
