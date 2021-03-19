#!/usr/bin/env python3
# coding: utf-8


def main():
    lis = [n for n in str(2**1000)]
    count = 0
    for i in lis:
        count += int(i)
    print(count)
    return


if __name__ == '__main__':
    main()
