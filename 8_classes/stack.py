#!/usr/bin/env python3
# coding: utf-8


class Verem:
    def __init__(self):
        self.li = []

    def __str__(self):
        return str(self.li)

    def betesz(self, o):
        self.li.append(o)

    def kivesz(self):
        return self.li.pop() if not self.ures() else None

    def meret(self):
        return len(self.li)

    def ures(self):
        return True if len(self.li) == 0 else False


class Sor:
    def __init__(self):
        self.li = []

    def __str__(self):
        return str(self.li)

    def enqueue(self, item):
        self.li.append(item)

    def dequeue(self):
        self.li.pop(0)


def main():
    v = Verem()
    print(v)
    print(v.ures())
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)
    print(v.meret())
    print(v.ures())
    x = v.kivesz()
    print(x)
    print(v)
    v.kivesz()
    v.kivesz()
    x = v.kivesz()
    print(x)

    print('-'*12)

    s = Sor()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s)
    s.dequeue()
    print(s)
    s.dequeue()
    s.dequeue()
    s.dequeue()
    print(s)


if __name__ == '__main__':
    main()
