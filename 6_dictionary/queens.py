#!/usr/bin/env python3
# coding: utf-8

def queens(pos):
    board_row = '. . . . . . . .'
    board = [board_row for i in range(8)]

    i = 0
    for p in pos:
        if p >= 8:
            print('Wrong arguments ... Chessboards are 8x8 squares!')
            return
        board[7-p] = board_row[:i*2] + 'Q' + board_row[i*2+1:]
        i += 1

    print('+-----------------+')
    for row in board:
        print('| ' + row + ' |')
    print('+-----------------+')


def main():
    queens([7, 3, 0, 2, 5, 1, 6, 4])
    queens([0, 4, 7, 5, 2, 6, 1, 3])
    queens([0, 4, 12, 5, 2, 9, 1, 3])


if __name__ == '__main__':
    main()
