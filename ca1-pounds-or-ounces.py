#!/usr/bin/env python3

pounds = int(input())
ounces = int(input())

total_pounds = pounds * 16

if total_pounds > ounces:
   print("pounds")
elif ounces > total_pounds:
   print("ounces")
elif ounces == total_pounds:
   print("same")
