#!/usr/bin/env python3
# coding: utf-8

def normalize(s):
    return ''.join(s.lower().split())


def annagramma(a, b):
    return True if sorted([c for c in normalize(a)]) == sorted([c for c in normalize(b)]) else False


def main():
    test(annagramma('listen', 'silent'), True)
    test(annagramma('A gentleman', 'Elegant man'), True)
    test(annagramma('Clint Eastwood', 'Old west action'), True)
    test(annagramma('dormitory', 'dirty room'), True)
    test(annagramma('Not Equal', 'Never will be'), False)
    test(annagramma('This will not work', 'So it does not'), False)
    return


"""Simple test method that prints expected and given
  items and checks if the two are equal or not"""


def test(got, expected):
    print('[{}] got: {}, expected: {}'.format(
        '✓' if got == expected else '✕', got, expected))


if __name__ == '__main__':
    main()
