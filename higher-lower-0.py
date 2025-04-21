#!/usr/bin/env python3

prev = int(input())
curr = int(input())
while curr and prev != 0:
   if prev > curr:
      print("lower")
   if prev == curr:
      print("equal")
   if prev < curr:
      print("higher")
   prev = curr
