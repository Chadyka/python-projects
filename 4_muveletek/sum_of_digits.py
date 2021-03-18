#!/usr/bin/env python3
# coding: utf-8

def sum_of_digits(start, end):
    nums = list(range(start, end+1))
    res = 0
    for num in nums:
        for digit in str(num):
            res += int(digit)
    return res


def main():
    start = input("Number to count from: ")
    end = input("Number to count to: ")

    print('Sum of numbers digits from {} to {} is {}'.format(
        start, end, sum_of_digits(int(start), int(end))))


if __name__ == "__main__":
    main()
