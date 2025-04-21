#!/usr/bin/env python3

s = input()
t = input()
v = input()

if len(s) > len(t) and len(s) > len(v):
   print(s)
elif len(t) > len(s) and len(t) > len(v):
   print(t)
elif len(v) > len(t) and len(v) > len(s):
   print(v)
