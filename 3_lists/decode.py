#!/usr/bin/env python3
# coding: utf-8


ENCODED_TEXT = """Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""

ABC = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'


def decode(s):
    result = ''
    for char in s:
        if char in ABC:
            result += ABC[(ABC.find(char) + 4) % len(ABC)]
        else:
            result += char
    return result


def main():
    print(decode(ENCODED_TEXT))
    return


if __name__ == '__main__':
    main()
