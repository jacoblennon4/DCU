#!/usr/bin/env python3

# Python program to print uppercase letters in the string

import re

# take input from the command line
string = input()
i = 0

while i < len(string):
   if (bool(re.match('[A-Z]', string[i]))):
      print(string[i])
   i = i + 1
