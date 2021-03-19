#!/usr/bin/env python3
# coding: utf-8

"""Calculates the median from a list of numbers
and returns the median which is the middle item
of a list if it has odd length and the average of
the 2 middle numbers if the list has even length"""


def median(nums):
    res = 0
    if len(nums) % 2 == 0:
        res = (sorted(nums)[len(nums)//2] + sorted(nums)[len(nums)//2-1])/2
    else:
        res = sorted(nums)[len(nums)//2]

    return res


"""Simple test method that prints expected and given
items and checks if the two are equal or not"""


def test(got, expected):
    if got == expected:
        prefix = 'OK'
    else:
        prefix = 'X'
    print('[{}] got: {}, expected: {}'.format(prefix, got, expected))


def main():
    test(median([1, 2, 3, 4, 5]), 3)
    test(median([3, 1, 2, 5, 3]), 3)
    test(median([1, 300, 2, 200, 1]), 2)
    test(median([3, 6, 20, 99, 10, 15]), 12.5)
    return


if __name__ == '__main__':
    main()
