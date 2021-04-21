#!/usr/bin/env python3
# coding: utf-8
from enum import Enum

LOW_LETTERS = "aáoóuú"
HIGH_LETTERS = "eéiíöőüű"


class Height(Enum):
    LOW = 1
    HIGH = 2
    MIXED = 3
    NEITHER = 4


def high_low(word):
    deeps = 0
    highs = 0
    for char in word:
        if char in list(LOW_LETTERS):
            deeps += 1
        elif char in list(HIGH_LETTERS):
            highs += 1

    if deeps > 0 and highs > 0:
        return Height.MIXED.name
    elif deeps > 0 and highs == 0:
        return Height.LOW.name
    elif deeps == 0 and highs > 0:
        return Height.HIGH.name
    elif deeps == 0 and highs == 0:
        return Height.NEITHER.name


def main():
    word = input("Give me a word: ")
    print('The given word "{}" is {}'.format(word, high_low(word)))


if __name__ == "__main__":
    main()
