#!/usr/bin/env python3

a = []
s = input()
while s != "end":
   a.append(s)
   s = input()
i = int(input())
j = i

while i < len(a):
   if int(a[i]) < int(a[j]):
      j = i
   i = i + 1
print(j)
