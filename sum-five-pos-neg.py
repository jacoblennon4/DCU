#!/usr/bin/env python3

i = 0
neg_total = 0
pos_total = 0
while i < 5:
   num = int(input())
   if num < 0:
      neg_total = num + neg_total
   else:
      pos_total = num + pos_total
   i = i + 1
print(neg_total, pos_total)
