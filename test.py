#!/usr/bin/env python3

# Usage:
# $ cat test.in | python3 test.py | diff - test.out


import sys


def main():
    for line in sys.stdin:
        if int(line) == 42:
            break
        print(line.rstrip())


if __name__ == '__main__':
    main()
