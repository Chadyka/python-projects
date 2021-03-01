#!/usr/bin/env python3
# coding: utf-8

import math

def verbing(s):
    if len(s) > 3 and s[-3:] == 'ing':
        return s + 'ly'
    elif len(s) > 3:
        return s + 'ing'
    else:
        return s


def not_bad(s):
    if s.find('not') < s.find('bad'):
        return s[:s.find('not')] + 'good' + s[s.find('bad') + 3:]
    return s


def front_back(a, b):
    return a[:math.ceil(len(a)/2)] + b[:math.ceil(len(b)/2)] + a[math.ceil(len(a)/2):] + b[math.ceil(len(b)/2):]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

#############################################################################


if __name__ == '__main__':
    main()
