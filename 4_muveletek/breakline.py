#!/usr/bin/env python3
# coding: utf-8

import sys
import random as r

UPTO = 10


def main():
    for i in range(UPTO):
        for j in range(10):
            print(r.randint(0, 9), end="")
        print("\n", end="")


if __name__ == "__main__":
    main()
