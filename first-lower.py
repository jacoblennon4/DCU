#!/usr/bin/env python3

prev = int(input())
curr = int(input())

while curr >= prev:
   prev = curr
   curr = int(input())
print(curr)
