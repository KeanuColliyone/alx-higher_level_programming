#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
def calculate(a, operator, b):
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return sub(a, b)
    elif operator == '*':
        return mul(a, b)
    elif operator == '/':
        if b == 0:
            return "Error: Division by zero"
        return div(a, b)
    else:
        return "Unknown operator. Available operators: +, -, * and /"
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    result = calculate(a, operator, b)
    if isinstance(result, str):
        print(result)
        sys.exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))
