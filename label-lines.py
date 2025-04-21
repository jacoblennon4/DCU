#!/usr/bin/env python3

a = []
s = input()
i = 0
while s != "end":
   a.append(s)
   s = input()
total_lines = len(a)
i = 0
while i < len(a):
   print(i, total_lines, a[i])
   i = i + 1
