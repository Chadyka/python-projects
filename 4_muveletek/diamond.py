#!/usr/bin/env python3
# coding: utf-8

def diamond(num):
    if num % 2 == 0:
        print("Diamond failed! Input has to be an odd number.")
    else:
        for i in range(1, num+1, 2):
            print(("*"*i).center(num))
        for i in range(num-2, -1, -2):
            print(("*"*i).center(num))


def main():
    diamond(int(input("Give me an odd number: ")))


if __name__ == "__main__":
    main()
