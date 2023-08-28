#!/usr/bin/python3

def safe_list_division(list_1, list_2, length):
    """
    Takes two lists and creates a new list with the result of division
    operation. Handles errors and prints error messages to stdout.
    """
    i = 0
    new_list = []
    result = 0
    for i in range(0, length):
        try:
            result = (list_1[i] / list_2[i])
        except TypeError:
            result = 0
            print("Error: Invalid data type")
        except ZeroDivisionError:
            result = 0
            print("Error: Division by zero")
        except IndexError:
            result = 0
            print("Error: Index out of range")
        finally:
            new_list.append(result)
    return new_list
