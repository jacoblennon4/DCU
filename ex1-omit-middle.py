#!/usr/bin/env python3

n = int(input())
a = []
c = []
while n != 0:
   a.append(n)
   n = int(input())
middle = len(a) // 2

i = 0
while i < len(a):
   if a[i] != a[middle]:
      c.append(a[i])
   i = i + 1
i = 0
while i < len(c):
   print(c[i])
   i = i + 1
