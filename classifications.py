#!/usr/bin/env python3

mark = int(input())

print("first:", mark >= 70)
print("second:", mark <= 69 and mark >= 50)
print("third:", mark <= 49 and mark >= 40)
print("fail:", mark < 40)
