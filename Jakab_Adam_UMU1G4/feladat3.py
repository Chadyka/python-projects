#!/usr/bin/env python3
# coding: utf-8


def main():
    file = open('numbers.csv', 'r')
    li = [st.split(';') for st in [s for s in file.read().split('\n')]]

    hun = []
    eng = []

    for line in li:
        line.pop()
        for s in line:
            if ',' in s:
                hun.append(float(s.replace(',', '.')))
            if '.' in s:
                eng.append(float(s))

    print(
        f"A fajlban {len(eng)} db angol és {len(hun)} db magyar szám található.")
    print(f'Az angol számok összege: {round(sum(eng), 2)}')
    print(f'A magyar számok összege: {round(sum(hun), 2)}')


if __name__ == '__main__':
    main()
