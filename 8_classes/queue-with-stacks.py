#!/usr/bin/env python3
# coding: utf-8

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def __str__(self):
        return str(self.s1)

    def append(self, x):
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(x)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def popleft(self):
        return self.s1.pop() if len(self.s1) != 0 else None

    def is_empty(self):
        return True if len(self.s1) == 0 else False

    def size(self):
        return len(self.s1)


def main():
    q = Queue()
    print(q.is_empty())
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    print(q.is_empty())
    q.popleft()
    print(q)
    print(q.size())
    q.popleft()
    q.popleft()
    print(q.size())
    q.popleft()
    print(q)
    print(q.size())
    print(q.is_empty())


if __name__ == '__main__':
    main()
