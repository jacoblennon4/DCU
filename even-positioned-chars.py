#!/usr/bin/env python3

s = input()
i = 0
t = ""
while i < len(s):
   if i % 2 == 0:
      t = t + s[i]
   i = i + 1
print(t)
