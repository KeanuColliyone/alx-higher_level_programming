#!/usr/bin/python3
import sys
arguments = sys.argv[1:]
total = sum(int(arg) for arg in arguments)
print(total)
