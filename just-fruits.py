#!/usr/bin/env python3

fruits = ["apple", "orange", "pear", "banana", "kiwi", "grapefruit"]
s = input()
i = 0
while s != "end":
   if s in fruits:
      print(s)
   s = input()
