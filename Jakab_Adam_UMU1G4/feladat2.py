#!/usr/bin/env python3
# coding: utf-8
import sys


def double_digits(s: str) -> str:
    li: list[str] = []
    for c in s:
        if c.isnumeric():
            li.append(c)
            li.append(c)
        else:
            li.append(c)

    return ''.join(li)


def main() -> None:
    if len(sys.argv) != 2:
        print('Hibás paraméterezés! Egyetelen sztringet kell megadni!')
        return
    print(double_digits(sys.argv[1]))


if __name__ == '__main__':
    main()
