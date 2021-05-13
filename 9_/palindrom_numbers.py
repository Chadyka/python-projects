
#!/usr/bin/env python3
# coding: utf-8

def decimal_to_binary(n):
    binary = ''
    if(n > 1):
        decimal_to_binary(n//2)
    binary += str(n % 2)
    print(binary, end='')


def palindrome_check(s):
    if s == s[::-1]:
        return True
    return False


def main():
    num = '585'
    print(num)

    if palindrome_check(num):
        num_in_binary = decimal_to_binary(num)
        if palindrome_check(num_in_binary):
            print('found a double palindrome')


if __name__ == '__main__':
    main()
