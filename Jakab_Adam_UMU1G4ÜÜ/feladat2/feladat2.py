#!/usr/bin/env python3
# coding: utf-8


def main():
    f = open('input.txt', 'r')
    s = f.read()
    f.close()
    level = 0
    d = {}

    path = []

    for bracket in s:
        if bracket == '(':
            level += 1
        elif bracket == ')':
            level -= 1
        path.append(level)
        d[level] = d.get(level, 0) + 1

    keys = list(d.keys())
    values = list(d.values())

    print('Célemelet: {}'.format(level))
    print('Legmélyebb emelet: {}'.format(min(path)))
    print('Legmagasabb emelet: {}'.format(max(path)))
    print('Legtöbbször érintett emelet: {}'.format(
        keys[values.index(max(values))]))


if __name__ == '__main__':
    main()
