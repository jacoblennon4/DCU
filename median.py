#!/usr/bin/env python3

a = []
s = input()
while s != "end":
    a.append(int(s))
    s = input()

i = 0
while i < len(a):
    p = i
    j = i + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j = j + 1
    tmp = a[p]
# remember the value at position p
    a[p] = a[i]
# move value at position i to p
    a[i] = tmp
    i = i + 1
median = len(a) // 2
print(a[median])

# i = position we want smallest number
# j = looks at each number after i to find smallest
# p = remembers the position of smallest number found
