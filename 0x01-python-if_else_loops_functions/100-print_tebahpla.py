#!/usr/bin/python3
for i in range(123, 96, -1):
    if i % 2 == 1:
        i = i - 32
    print("{:c}".format(i), end="")
