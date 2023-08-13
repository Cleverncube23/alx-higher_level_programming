#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Return list with True/False if num in my_list is divisible by 2"""
    
    bool_list = []
    for num in my_list:
        if num % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
            
    return bool_list
