#!/usr/bin/env python3

a = []
s = input()
count = 0
i = 0
while s != "end":
   a.append(int(s))
   count = int(s) + count
   s = input()
if len(a) > 0:
   #So before we try to find the average,
   #we check if there are any numbers inside the list.
   #If there are, we do the math.
   #If there aren’t, we just skip it to avoid an error.
   average = count // len(a)

i = 0
while i < len(a):
   if a[i] < average:
      print(a[i])
   i = i + 1
