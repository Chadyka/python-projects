#!/usr/bin/env python3
# coding: utf-8


def product(numbers):
    prod_of_nums = 1
    for num in numbers:
        prod_of_nums *= num
    return prod_of_nums


def main():
    numbers = [2, 3, 5, 7, 11, 13]
    print(product(numbers))


if __name__ == '__main__':
    main()
