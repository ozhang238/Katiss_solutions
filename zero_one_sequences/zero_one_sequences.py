#!/usr/bin/python
from sys import stdin

def main():
    M = 1000000007
    total = 0
    ones = 0
    branches = 1
    for char in stdin.readline():
        if char == '?': 
            total       = ( (total<<1) % M + ones) % M
            ones        = ( (ones<<1) % M + branches) % M
            branches    = (branches<<1) % M
        elif char == '0':
            total = ( total + ones   ) % M
        else:
            ones  = ( ones  + branches ) % M

    print(total)

if __name__ == "__main__":
    main()
