#!/usr/bin/env python3
# coding: utf-8


def munchausen_nums(end):
    result = [num for num in range(end) if sum(
        0 if int(digit) == 0 else int(digit) ** int(digit) for digit in str(num)) == num]
    print("Munchausen numbers up to {} are: ".format(end), result, "\n")


def main():
    munchausen_nums(100000)
    munchausen_nums(440000000)


if __name__ == "__main__":
    main()
