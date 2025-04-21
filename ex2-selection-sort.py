#!/usr/bin/env python3

a = []
n = int(input())
while n != 0:
  a.append(n)
  n = int(input())
i = 0
while i < len(a):
    p = i
    j = i + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j = j + 1
    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp
    i = i + 1

# Code omitted 3... write the list to standard output, one value per line.
# j checks every number after i, it finds the smallest number after i
# p stores the position of the smallest number found while j goes around,
# at the end of the loop p and a[i] swap
# i is the position you want to swap the smallest num to
i = 0
while i < len(a):
    print(a[i])
    i = i + 1
