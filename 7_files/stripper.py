#!/usr/bin/env python3
# coding: utf-8


def main():
    inp_file = open("string1.py", "r")
    out_file = open("string1_clean.py", "w")
    for line in inp_file:
        if(line.find('#') == -1):
            print(line, file=out_file, end='')
    inp_file.close()
    out_file.close()


if __name__ == '__main__':
    main()
