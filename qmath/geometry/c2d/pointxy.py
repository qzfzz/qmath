#!/bin/env python3
# coding:utf-8
# author bruce


class PointXY:
    x = None
    y = None

    def __init__(self, x, y):
        assert(x is not None)
        assert(y is not None)

        self.x = x
        self.y = y

    def __str__(self):
        return "(x, y) => (" + str(self.x) + ", " + str(self.y) + ")"


def test():

    """test fo __str__"""

    pointxy = PointXY(1, 2)
    print(pointxy)


if __name__ == '__main__':
    test()

