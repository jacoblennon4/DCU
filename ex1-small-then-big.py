#!/usr/bin/env python3

n = int(input())
big = []
while n != 0:
   if n < 100:
      print(n)
   else:
      big.append(n)
   n = int(input())
i = 0
while i < len(big):
   print(big[i])
   i = i + 1
