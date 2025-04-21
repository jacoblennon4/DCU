#!/usr/bin/env python3

if __name__ == "__main__":
    a = [49, 32, 39, 13, 30, 12, 14, 12, 31, 31]

i = 0
j = 1

while j < len(a):
  if a[j] < a[i]:
      i = j
  j = j + 1

print(i)
