#!/usr/bin/env python3

s = input()
while s != "end":
   i = 0
   while s[i] != " ":
      i = i + 1
   name = s[:i]
   num = int(s[i + 1:])
   print(name, num * 25)

   s = input()
