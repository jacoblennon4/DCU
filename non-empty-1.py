#!/usr/bin/env python3

if __name__ == "__main__":
   a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]

i = 0
count = 0
while i < len(a):
   if len(a[i]) > 0:
      count = count + 1
   i = i + 1
print(count)
