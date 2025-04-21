#!/usr/bin/env python3

s = input()
i = 0
j = 0
while i < len(s) and not ("0" <= s[i] <= "9"):
   i = i + 1
if i < len(s):
   j = i
   while j < len(s) and "0" <= s[j] <= "9":
      j = j + 1
   print(s[i:j], i)
