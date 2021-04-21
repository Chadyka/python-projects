#!/usr/bin/env python3
# coding: utf-8


def brackets(s):
    brackets = {'(': ')', '[': ']', '{': '}'}
    li = [c for c in s if c in ['(', ')', '[', ']', '{', '}']]

    right = [br for br in li if br not in brackets]
    left = [br for br in li if br in brackets]
    if len(right) != len(left):
        return False

    idx = 0
    for i, br in enumerate(li, 0):
        if br in [')', ']', '}']:
            idx = i
            break
    for i in range(idx, len(li)-1):
        for j in range(idx-1, 0, -1):
            if li[i] != brackets[li[j]]:
                return False
            else:
                idx -= 1
                break
    return True


def main():
    tests_inp = ["((5+3)*2+1)", "{[(3+1)+2]+}", "(3+{1-1)}",
                 "[1+1]+(2*2)-{3/3}", "(({[(((1)-2)+3)-3]/3}-3)"]
    test(brackets(tests_inp[0]), True)
    test(brackets(tests_inp[1]), True)
    test(brackets(tests_inp[2]), False)
    test(brackets(tests_inp[3]), True)
    test(brackets(tests_inp[4]), False)


"""Simple test method that prints expected and given
  items and checks if the two are equal or not"""


def test(got, expected):
    print('[{}] got: {}, expected: {}'.format(
        '✓' if got == expected else '✕', got, expected))


if __name__ == '__main__':
    main()
