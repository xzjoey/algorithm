#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function
def main():
    print('Hello', sys.argv[0])
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself

if __name__ == '__main__':
    main()
