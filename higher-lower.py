#!/usr/bin/env python3

i = 0
prev = int(input())
while i < 5:
   curr = int(input())
   if prev > curr:
      print("lower")
   if prev == curr:
      print("equal")
   if prev < curr:
      print("higher")
   prev = curr
   i = i + 1
