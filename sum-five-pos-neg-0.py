#!/usr/bin/env python3

neg_total = 0
pos_total = 0

while sum != 0:
   sum = int(input())
   if sum < 0:
      neg_total = neg_total + sum
   else:
      pos_total = pos_total + sum
print(neg_total, pos_total)
