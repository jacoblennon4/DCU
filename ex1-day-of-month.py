#!/usr/bin/env python3

s = input()
i = 0

while s[i] != "/":
   i = i + 1
if i < len(s):
   print(s[:i])
