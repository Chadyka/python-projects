#!/usr/bin/env python3
# coding: utf-8

def reverse_num(number):
    return int(str(number)[::-1])


def main():
    num = 324526
    return print(reverse_num(num))


if __name__ == '__main__':
    main()
