#!/usr/bin/python3
"""Reads from standard input and computes metrics.
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


import sys

def print_stats(total_size, status_codes):
    """Prints statistics"""
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{:d}: {:d}".format(code, status_codes[code]))

line_count = 0
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        try:
            line_parts = line.split()
            total_size += int(line_parts[-1])
            status_code = int(line_parts[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1
        except Exception:
            pass

        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise
