#!/usr/bin/env python3
# coding: utf-8

def reverse_num(number):
    return int(str(number)[::-1])


def main():
    num = input("Number to reverse: ")
    return print(reverse_num(num))


if __name__ == '__main__':
    main()
