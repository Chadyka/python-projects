#!/usr/bin/env python3
# coding: utf-8

def dec_to_bin(num):
    res = ""
    while (num > 0):
        if (num % 2 == 0):
            res += "0"
        else:
            res += "1"
        num = int(num/2)
    return res[::-1]


def main():
    num = int(input("Give me a decimal number: "))
    print("{} in binary: ".format(num), dec_to_bin(num))


if __name__ == "__main__":
    main()
