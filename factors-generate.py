#!/usr/bin/python3
"""
Module that factorizes
nums into product
"""
from sys import argv


def factorize(value):
    """"decomposition of int > 1"""
    i = 2

    if value < 2:
        return
    factors = []
    while i * i <= value:
        if value % i:
            i += 1
        else:
            value //= i
            factors.append(i)
    if value > 1:
        factors.append(value)
    print(f"{value} = {' * '.join(map(str, factors))}")


if len(argv) != 2:
    exit()

try:
    with open(argv[1]) as file:
        line = file.readline()

        while line != "":
            value = int(line.split('\n')[0])
            factorize(value)
            line = file.readline()
except:
    pass

