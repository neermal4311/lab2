#!/usr/bin/env python3

# Author: Ngautam11
# Author ID: ngautam11
# Date Created: 2024/09/24

import sys

# Check the number of command line arguments
if len(sys.argv) > 1:
    timer = int(sys.argv[1])  # Convert the command line argument to an integer
else:
    timer = 3  # Default value if no argument is provided

# WHILE loop to count down
while timer > 0:
    print(timer)
    timer -= 1  # Decrement the timer

# Print the final message
print('blast off!')
