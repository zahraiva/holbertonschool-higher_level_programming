#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number < 0:
    lastdigit = -lastdigit
print(f"Last digit of {number} is {lastdigit} and", end=' ')
if lastdigit > 5:
    print("is greater than 5")
elif lastdigit == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")
