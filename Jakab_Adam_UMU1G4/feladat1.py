#!/usr/bin/env python3
# coding: utf-8


def main():
    file = open('f1_pelda.txt', 'r')
    li = [st.split(': ') for st in [s for s in file.read().split('\n')]]
    counter = 0

    for line in li:
        rule = [c for c in line[0].replace(' ', '-').split('-')]
        if rule[2] == line[1][int(rule[0])-1] or rule[2] == line[1][int(rule[1])-1]:
            counter += 1
    print(counter)


if __name__ == '__main__':
    main()
