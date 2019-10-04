#!/usr/bin/env python3

# Usage:
# $ echo '1 2 88 42 99' | python3 test.py


import sys


def main():
    data = map(int, sys.stdin.readline().split())
    for elt in data:
        if elt == 42:
            break
        print(elt)


if __name__ == '__main__':
    main()
