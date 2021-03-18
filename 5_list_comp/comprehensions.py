#!/usr/bin/env python3
# coding: utf-8

"""List comprehesion for printing first
letter of each word in the given string."""


def ex_8():
    res = [subs[0] for subs in 'python is an awesome language'.split()]
    print(res)


"""List comprehension for printing a tuple as (word, word length)"""


def ex_9():
    s = 'The quick brown fox jumps over the lazy dog'
    i = 0
    res = [(subs, len(subs)) for subs in s.split()]
    print(res)


"""List comprehension for printing even numbers up to 10"""


def ex_10():
    res = [x for x in range(10) if x % 2 == 0]
    print(res)


"""List comprehension for printing even squared numbers up to 20"""


def ex_11():
    res = [x**2 for x in range(20) if x**2 % 2 == 0]
    print(res)


"""List comprehension for printing squared numbers
which end with the digit 4 up to 20"""


def ex_12():
    res = [x**2 for x in range(20) if x**2 % 10 == 4]
    print(res)


"""List comprehension for printing the alphabet
with the use of chr() and the unicode alphabet"""


def ex_13():
    res = [chr(i) for i in range(65, 90)]
    print(''.join(res))


"""List comprehension for printing the list items
without whitespaces"""


def ex_14():
    lis = [' apple ', ' banana ', ' kiwi']
    res = [''.join(s.split()) for s in lis]
    print(res)


"""List comprehension for printing the
given list as a joined string"""


def ex_15():
    lis = [1, 0, 1, 1, 0, 1, 0, 0]
    res = [str(x) for x in lis]
    print(''.join(res))


def main():
    ex_8()
    print()
    ex_9()
    print()
    ex_10()
    print()
    ex_11()
    print()
    ex_12()
    print()
    ex_13()
    print()
    ex_14()
    print()
    ex_15()
    print()
    return


if __name__ == '__main__':
    main()
