#!/usr/bin/env python3
# coding: utf-8


def main():
    file = open('szoveg.txt', 'r')
    li = [st.split(' ') for st in [s for s in file.read().split('\n')]]

    for line in li:
        for s in line:
            if s == s[::-1]:
                print(s, end='')
            else:
                for i in range(len(s)):
                    print('X', end='')
            print(' ', end='')
        print()


if __name__ == '__main__':
    main()
