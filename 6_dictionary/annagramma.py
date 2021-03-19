#!/usr/bin/env python3
# coding: utf-8

def normalize(s):
    return ''.join(s.lower().split())


def annagramma(a, b):
    s1 = [c for c in normalize(a)]
    s2 = [c for c in normalize(b)]
    return True if sorted(s1) == sorted(s2) else False


"""Simple test method that prints expected and given
items and checks if the two are equal or not"""


def test(got, expected):
    if got == expected:
        prefix = '✓'
    else:
        prefix = '✕'
    print('[{}] got: {}, expected: {}'.format(prefix, got, expected))


def main():
    test(annagramma('listen', 'silent'), True)
    test(annagramma('A gentleman', 'Elegant man'), True)
    test(annagramma('Clint Eastwood', 'Old west action'), True)
    test(annagramma('dormitory', 'dirty room'), True)
    test(annagramma('Not Equal', 'Never will be'), False)
    test(annagramma('This will not work', 'So it does not'), False)
    return


if __name__ == '__main__':
    main()
