#!/usr/bin/python3
"""Reads from standard input and computes metrics
"""


import sys
import signal

"""Initialize variables to store metrics"""
total_file_size = 0
status_code_counts = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
        404: 0, 405: 0, 500: 0}
lines_processed = 0


def print_metrics():
    print("Total file size:", total_file_size)
    for status_code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")
    sys.stdout.flush()


def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)


"""Register signal handler for keyboard interruption"""
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        """Split the line into its components"""
        parts = line.strip().split()
        """Extract file size and status code"""
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        """Update metrics"""
        total_file_size += file_size
        status_code_counts[status_code] += 1
        lines_processed += 1

        """Print metrics every 10 lines"""
        if lines_processed % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    """Print final metrics if interrupted by keyboard"""
    print_metrics()
