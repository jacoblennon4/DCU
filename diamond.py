#!/usr/bin/env python3

import sys
n = int(sys.argv[1])
i = 0
half = n // 2
while i < half:
   print(" " * (half - i) + "*" * (2 * i + 1))
   i = i + 1

print("*" * n)

i = half - 1
while i >= 0:
   print(" " * (half - i) + "*" * (2 * i + 1))
   i = i - 1
