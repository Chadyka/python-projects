#!/usr/bin/env python3
# coding: utf-8
import sys


def trivial(s):
    if s == s[::-1]:
        return True
    return False


def _while_(s):
    i = 0
    comp = s[::-1]
    while i < len(s):
        if s[i] == comp[i]:
            i += 1
        else:
            return False
    return True


def recursive(s, comp, pos):
    if s[pos] == comp[pos]:
        if pos == len(s)-1:
            return True
        return recursive(s, comp, pos+1)
    return False


def main():
    if len(sys.argv) != 2:
        print('Please define a strategy from [ trivial, while, resursive ]')
        return

    inp = input("Give me a word: ")
    if sys.argv[1] == 'trivial':
        print(trivial(inp))
    elif sys.argv[1] == 'while':
        print(_while_(inp))
    elif sys.argv[1] == 'recursive':
        print(recursive(inp, inp[::-1], 0))


if __name__ == '__main__':
    main()
