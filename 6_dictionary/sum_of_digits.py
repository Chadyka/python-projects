#!/usr/bin/env python3
# coding: utf-8


def main():
    print('sum of digits from 2 to the power of 1000 is: {}'.format(
        sum([int(n) for n in str(2**1000)])))


if __name__ == '__main__':
    main()
