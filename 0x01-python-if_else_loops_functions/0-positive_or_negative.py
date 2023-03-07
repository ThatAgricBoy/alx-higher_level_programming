#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number >= -10 and number <= -1:
    print(f"{number:d} is negative")
elif number >= 1 and number <= 10:
    print(f"{number:d} is positive")
else:
    print(f"{number:d} is zero")
