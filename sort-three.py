#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

if a > b:
   a, b = b, a
if a > c:
   a, c = c, a

if b > c:
   b, c = c, b

print(a)
print(b)
print(c)
