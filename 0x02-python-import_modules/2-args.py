#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name from the arguments
    
    num_args = len(argv)
    
    if num_args == 0:
        argStr = "0 argument."
    elif num_args == 1:
        argStr = "1 argument: {}:".format(argv[0])
    else:
        argStr = "{} arguments: {}:".format(num_args, ", ".join(argv))
    
    print(argStr)
    
    for i, arg in enumerate(argv, start=1):
        print(i, ":", arg)

