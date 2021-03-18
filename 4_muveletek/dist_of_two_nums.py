#!/usr/bin/env python3
# coding: utf-8

import math


def dist_of_two_nums(point_1, point_2):
    a = point_1[0]-point_2[0]
    b = point_1[1]-point_2[1]
    result = math.sqrt(a**2+b**2)
    return result


def main():
    inp_1 = input("Give me the coordinates of point_1 as x,y : ")
    inp_2 = input("Give me the coordinates of point_2 as x,y : ")
    point_1 = (int(inp_1.split(',')[0]), int(inp_1.split(',')[1]))
    point_2 = (int(inp_2.split(',')[0]), int(inp_2.split(',')[1]))
    print('Distance between {} and {} is {}'.format(
        point_1, point_2, dist_of_two_nums(point_1, point_2)))


if __name__ == "__main__":
    main()
