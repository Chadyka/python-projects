#!/usr/bin/env python3
# coding: utf-8

def sum_of_squares():
    res = 0
    for i in range(1, 101):
        res += i**2
    return res


def square_of_sum():
    res = 0
    for i in range(1, 101):
        res += i
    return res**2


def main():
    print("Difference between square of sum and sum of squares is ",
          square_of_sum()-sum_of_squares())


if __name__ == "__main__":
    main()
