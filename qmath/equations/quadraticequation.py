#!/bin/env python3
# coding:utf-8


class QuadraticEquation:
    a = 0
    b = 0
    c = 0

    def __init__(self, a=0, b=0, c=0):

        assert(a is not None and a != 0)

        self.a = a
        self.b = b
        self.c = c

    def get_root(self):
        delta = self.get_delta()

        root_cnt = self.root_count()

        if 0 == root_cnt:
            raise Exception('no root for the equation')

        if root_cnt == 1:
            return -self.b / (2.0 * self.a)

        x1 = (-self.b + pow(delta, 0.5))/(2 * self.a)
        x2 = (-self.b - pow(delta, 0.5)) / (2 * self.a)

        return (x1, x2)

    def get_delta(self):
        return pow(self.b, 2) - 4 * self.a * self.c

    def has_root(self):
        delta = self.get_delta()

        if delta < 0:
            return False
        return True

    def root_count(self):
        delta = self.get_delta()

        if delta < 0:
            return 0
        elif 0 == delta:
            return 1
        else:
            return 2


def test():
    equation = QuadraticEquation(1,0,-1)
    print(equation.get_root())


if '__main__' == __name__:
    test()

