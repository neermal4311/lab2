#!/usr/bin/env python3

import sys

# Ensure at least two arguments are provided
if len(sys.argv) < 3:
    print("Not enough arguments provided.")
    sys.exit(1)

name = sys.argv[1]  # first argument as string
age = int(sys.argv[2])  # second argument as integer

print(f'Hi {name}, you are {age} years old.')
