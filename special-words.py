#!/usr/bin/env python3

special = []
s = input()
while s != "end":
   special.append(s)
   s = input()
h = input()
while h != "end":
   if h in special:
      print(h)
   h = input()
