#!/usr/bin/python3

def safe_print_division(numberator, denominator):
    """
    Divides two integers and prints the result.
    Catches divide by zero exception.
    """
    try:
        result = numberator / denominator
    except:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
