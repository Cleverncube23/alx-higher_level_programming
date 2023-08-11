#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name from the arguments
    
    total_sum = sum(int(arg) for arg in argv)
    
    print(total_sum)
else:
    argc = len(sys.argv) - 1
    
    i = 0
    result = 0
    for arg in sys.argv:
        if i != 0:
            result += int(arg)
        else:
            i += 1
    print("{:d}".format(result))

