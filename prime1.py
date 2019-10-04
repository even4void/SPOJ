#!/usr/bin/env python3

# Usage:
# $ cat test.in | python3 prime1.py | diff - test.out


import sys
from sympy import sieve


def primes(range):
    return list(sieve.primerange(range[0], range[1]+1))


def main():
    data = sys.stdin.readlines()
    iter = int(data[0].rstrip())
    for val in data[1:]:
        lst = primes(list(map(int, val.split())))
        print("\n".join([str(elt) for elt in lst]), end="\n\n")


if __name__ == '__main__':
    main()
