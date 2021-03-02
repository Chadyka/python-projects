#!/usr/bin/env python3
# coding: utf-8


def remove_whitespace(s):
    return ''.join(s.split())


def main():
    ips = ["192.20.246.138:\n6666", "206.130.99.82:\n8080",
           "16\n\n5.59.1\r45.        122:\t8000"]
    for ip in ips:
        print(remove_whitespace(ip))


if __name__ == '__main__':
    main()
