#!/usr/bin/python3

from fractions import gcd
from sys import argv

def pollards_rho(n):
    x = 2
    y = 2
    d = 1
    f = lambda x: (x**2 - 2) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    if d != n:
        return d

def read_file(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                print(f"Difference: {line1.strip()} | {line2.strip()}")

if __name__ == "__main__":
    if len(argv) == 3:
        read_file(argv[1], argv[2])
    else:
        print("Please provide two file paths to compare.")

