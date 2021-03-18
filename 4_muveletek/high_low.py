#!/usr/bin/env python3
# coding: utf-8

LOW = "aáoóuú"
HIGH = "eéiíöőüű"


def high_low(word):
    deeps = 0
    highs = 0
    for char in word:
        if char in list(LOW):
            deeps += 1
        elif char in list(HIGH):
            highs += 1

    if deeps & highs > 0:
        return "mixed"
    elif deeps > 0 and highs == 0:
        return "low"
    elif deeps == 0 and highs > 0:
        return "high"
    elif deeps == 0 and highs == 0:
        return "neither"


def main():
    word = input("Give me a word: ")
    print('The given word "{}" is {}'.format(word, high_low(word)))


if __name__ == "__main__":
    main()
