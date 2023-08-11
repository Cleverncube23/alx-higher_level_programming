#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name from the arguments
    
    num_args = len(argv)
    
    if num_args == 0:
        print("0 argument.")
    elif num_args == 1:
        print("1 argument:", argv[0] + ":")
        print("1:", argv[0])
    else:
        print(num_args, "arguments:", ", ".join(argv) + ":")
        for i, arg in enumerate(argv, start=1):
            print(i, ":", arg)
