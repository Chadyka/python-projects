#!/usr/bin/env python3
# coding: utf-8
import math


def main():
    f = open('input.txt', 'r')
    lines = f.readlines()
    d = dict([s.split(';') for s in lines])
    indexes = sorted([int(n) for n in d.keys() if math.sqrt(int(n)) % 1 == 0])

    res = ''

    for i in indexes:
        res += d[str(i)][0]

    print(res.replace('_', ' '))


if __name__ == '__main__':
    main()
