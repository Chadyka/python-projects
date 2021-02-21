#!/usr/bin/env python3
# coding: utf-8


# Az isdigit() string metódus True értéket ad ha csak számjegyekből
# áll a string amire meghívtuk, ellenkező esetben False értéket
def main():
    num = input("Give me a number: ")
    print('Thanks, ' + str(num) +
          ' is a number') if num.isdigit() else print('That is not a number!')


if __name__ == '__main__':
    main()
