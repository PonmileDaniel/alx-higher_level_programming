#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

import sys
import re
from collections import defaultdict

def extract_size_and_status(line):
    """Extract size and status code from a line."""
    try:
        size = int(re.search(r'\d+$', line).group())
        status_code = re.search(r'\b\d{3}\b', line).group()
        return size, status_code
    except AttributeError:
        return None, None

def print_stats(size, status_codes):
    """Print accumulated metrics."""
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    size = 0
    status_codes = defaultdict(int)

    try:
        for i, line in enumerate(sys.stdin, start=1):
            if i % 10 == 0:
                print_stats(size, status_codes)

            line_size, status = extract_size_and_status(line)
            if line_size is not None:
                size += line_size
                if status in ['200', '301', '400', '401', '403', '404', '405', '500']:
                    status_codes[status] += 1

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
