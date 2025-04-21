#!/usr/bin/env python3

n = int(input())
i = 0
sign = 1
while i < n:
   print(i * sign)
   sign = sign * -1
   i = i + 1
