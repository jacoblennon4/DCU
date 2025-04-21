#!/usr/bin/env python3

s = input()
i = 0
while s[i] != "+":
   i = i + 1
   if i < len(s):
      j = i + 1
a = int(s[:i])
b = int(s[j:])
print(a + b)
