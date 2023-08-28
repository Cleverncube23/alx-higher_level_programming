#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """
    Prints an integer using the format "{:d}".

    If a TypeError or ValueError is caught, an error message is printed
    to the standard error.

    Args:
        value (int): The integer to be printed.

    Returns:
        bool: True if the integer is printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False

