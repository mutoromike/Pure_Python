"""
This is a task that implements fibonacci series using
ARGPARSE:
"""

import argparse


def fibn(n):

    a, b = 0, 1

    for i in range(n):
        a, b = b, a+b

    return a


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", help="The fibonacci number", type=int)
    args = parser.parse_args()
    results = fibn(args.num)

    print("The "+str(args.num)+"th fibonacci number is "+str(results))


if __name__ == "__main__":
    Main()
