#!/usr/bin/env python3

side = int(input())
radius = int(input())

area_of_square = side * side
area_of_circle = 3.14 * radius * radius

if area_of_square < area_of_circle:
   print("circle")
elif area_of_circle < area_of_square:
   print("square")
else:
   print("same")
