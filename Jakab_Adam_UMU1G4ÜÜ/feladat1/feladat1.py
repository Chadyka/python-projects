#!/usr/bin/env python3
# coding: utf-8
import sys


def main():
    if len(sys.argv) != 4:
        return print('Hiba! Adj meg pontosan három sztringet!')

    li = sys.argv
    li.remove('feladat1.py')

    max_len = max([len(s) for s in li])
    x = 'X'*max_len
    li_fin = []

    for s in li:
        if len(s) < max_len:
            s = s + x[len(s):]
        li_fin.append(s)

    final = ''

    for i in range(max_len):
        for j in range(3):
            final += li_fin[j][i]

    print(final)


if __name__ == '__main__':
    main()
