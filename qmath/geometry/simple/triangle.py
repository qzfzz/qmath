#!/bin/env python3
# coding:utf-8


class Triangle:

    @staticmethod
    def get_area(side_a, side_b, side_c):

        if not Triangle.is_triangle_valid(side_a, side_b, side_c):
            raise Exception('invalid triangle')

        p = (side_a + side_b + side_c) / 2

        area = pow(p * (p - side_a) * (p - side_b) * (p - side_c), 0.5)

        return area

    @staticmethod
    def is_triangle_valid(side_a, side_b, side_c):
        if side_a + side_b > side_c and side_b + side_c > side_a and side_c + side_a > side_b:
            return True

        return False


def test(side_a, side_b, side_c):
    return Triangle.get_area(side_a, side_b, side_c)


if '__main__' == __name__:
    assert(test(3, 4, 5) == 6)





