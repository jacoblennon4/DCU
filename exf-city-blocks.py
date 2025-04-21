#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x2 > x1:
   A = x2 - x1
else:
   A = x1 - x2
if y2 > y1:
   B = y2 - y1
else:
   B = y1 - y2

distance = A + B
print(distance)
