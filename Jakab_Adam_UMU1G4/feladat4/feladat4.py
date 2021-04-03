#!/usr/bin/env python3
# coding: utf-8


def fibonacci():
    num_1 = 0
    num_2 = 1
    fib = 0
    fib_sum = 0

    while fib <= 4000000:
        fib = num_1 + num_2
        num_1 = num_2
        num_2 = fib
        if fib % 2 == 0:
            fib_sum += fib
    return fib_sum


def main():
    print("Fibonacci sequence's sum of even numbers up to 4 billion: {}".format(
        fibonacci()))


if __name__ == '__main__':
    main()
