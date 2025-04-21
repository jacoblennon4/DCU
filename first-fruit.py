#!/usr/bin/env python3

s = input()
fruits = ("orange", "apple", "banana")
while s not in fruits:
   s = input()
print(s)

#previously used "while s not fruits" , that doesnt work as itll look for all 3
#if you use not in, it looks inside the list for each individual one
