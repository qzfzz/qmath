#!/bin/env python3
# coding:utf-8
# author bruce

from qmath.geometry.c2d.lineequation import LineEquation
from qmath.geometry.c2d.pointxy import PointXY


class Vector:

    """
    we define a vector like this
                    left side(-1)
    begin_point -----------------> end_point
                    right side(1)
    """

    LEFT_SIDE = -1
    RIGHT_SIDE = 1
    ON_LINE = 0

    begin_point = None
    end_point = None

    # line equation for vector
    line_equation = None

    def __init__(self, begin_point, end_point):
        self.begin_point = begin_point
        self.end_point = end_point

        line_equation = LineEquation.get_line_equation_from_two_points(begin_point, end_point)
        self.line_equation = line_equation

    def is_point_on_vector(self, point):
        """
        point on line
        """

        assert(point)

        if self.line_equation.k is not None:
            if point.y == self.line_equation.k * point.x + self.line_equation.b:
                return True
            else:
                return False

        if not self.line_equation.k:

            if self.line_equation.x and point.x == self.line_equation.x:
                return True

            if self.line_equation.y and point.y == self.line_equation.y:
                return True

        return False

    def is_point_in_vector(self, point):
        """
        point in vector
        :param point:
        :return:
        """
        assert(point)

        if not self.is_point_on_vector(point):
            return False

        left_x = self.end_point.x if self.end_point.x < self.begin_point.x else self.begin_point.x
        right_x = self.end_point.x if self.end_point.x > self.begin_point.x else self.begin_point.x

        bottom_y = self.end_point.y if self.end_point.y < self.begin_point.y else self.begin_point.y
        top_y = self.end_point.y if self.end_point.y > self.begin_point.y else self.begin_point.y

        if point.x >= left_x and point.x <= right_x and point.y >= bottom_y and point.y <= top_y:
            return True

        return False

    def get_point_on_side_of_vector(self, point):
        """
        point on which side of vector
        :param point:
        :return: -1 for left side 1 for right side 0 for on line
        """
        assert(point)

        if self.is_point_on_vector(point):
            return Vector.ON_LINE

        if self.line_equation.getK() > 0 and self.begin_point.x < self.end_point.x:
            foot_point = self.line_equation.get_foot_point_of_line(point)

            if point.x < foot_point.x:
                return Vector.LEFT_SIDE
            elif point.x > foot_point.x:
                return Vector.RIGHT_SIDE
            else:
                return Vector.ON_LINE

        if self.line_equation.getK() > 0 and self.begin_point.x > self.end_point.x:
            foot_point = self.line_equation.get_foot_point_of_line(point)

            if point.x < foot_point.x:
                return Vector.RIGHT_SIDE
            elif point.x > foot_point.x:
                return Vector.LEFT_SIDE
            else:
                return Vector.ON_LINE

        if self.line_equation.getK() < 0 and self.begin_point.x > self.end_point.x:
            foot_point = self.line_equation.get_foot_point_of_line(point)

            if point.x < foot_point.x:
                return Vector.LEFT_SIDE
            elif point.x > foot_point.x:
                return Vector.RIGHT_SIDE
            else:
                return Vector.ON_LINE

        if self.line_equation.getK() < 0 and self.begin_point.x < self.end_point.x:
            foot_point = self.line_equation.get_foot_point_of_line(point)

            if point.x < foot_point.x:
                return Vector.RIGHT_SIDE
            elif point.x > foot_point.x:
                return Vector.LEFT_SIDE
            else:
                return Vector.ON_LINE

        if self.line_equation.getY() and self.begin_point.x < self.end_point.x:
            foot_point = self.line_equation.get_foot_point_of_line(point)

            if point.y < foot_point.y:
                return Vector.RIGHT_SIDE
            elif point.y > foot_point.y:
                return Vector.LEFT_SIDE
            else:
                return Vector.ON_LINE

        if self.line_equation.getY() and self.begin_point.x > self.end_point.x:
            foot_point = self.line_equation.get_foot_point_of_line(point)

            if point.y < foot_point.y:
                return Vector.LEFT_SIDE
            elif point.y > foot_point.y:
                return Vector.RIGHT_SIDE
            else:
                return Vector.ON_LINE

        if self.line_equation.getX() and self.begin_point.y < self.end_point.y:
            foot_point = self.line_equation.get_foot_point_of_line(point)

            if point.x < foot_point.x:
                return Vector.LEFT_SIDE
            elif point.x > foot_point.x:
                return Vector.RIGHT_SIDE
            else:
                return Vector.ON_LINE

        if self.line_equation.getX() and self.begin_point.y > self.end_point.y:
            foot_point = self.line_equation.get_foot_point_of_line(point)

            if point.x < foot_point.x:
                return Vector.RIGHT_SIDE
            elif point.x > foot_point.x:
                return Vector.LEFT_SIDE
            else:
                return Vector.ON_LINE

        raise Exception('unknown exception')

    def __str__(self):
        return '(' + str(self.begin_point.x) + ', ' + str(self.begin_point.y) + \
               ') -> (' + \
               str(self.end_point.x) + ', ' + str(self.end_point.y) + ')'


if __name__ == '__main__':
    vector = Vector(PointXY(1, 1), PointXY(2, 2))
    print(vector)
    print(vector.is_point_on_vector(PointXY(3, 3)))

    print(vector.is_point_in_vector(PointXY(3, 3)))
    print(vector.is_point_in_vector(PointXY(1.5, 1.5)))