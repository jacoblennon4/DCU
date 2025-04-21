#!/usr/bin/env python3

s = input()
t = ""

i = 0
while i < len(s):
    t = s[i] + t
    i = i + 1
if s == t:
    print("palindrome")
