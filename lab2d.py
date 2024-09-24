#!/usr/bin/env python3

import sys

# Check for zero or incorrect number of arguments
if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} name age')
    sys.exit()

name = sys.argv[1]  # first argument as string
age = sys.argv[2]  # second argument as string

print(f'Hi {name}, you are {age} years old.')

