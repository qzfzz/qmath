#!/bin/env python3
# coding:utf-8
# author bruce

from qmath.geometry.c2d.pointxy import PointXY
import math

class LineEquation:
    """
    line equation
    """
    k = None
    b = None
    x = None
    y = None

    def __init__(self, k=None, b=None, x=None, y=None):
        self.k = k
        self.b = b
        self.x = x
        self.y = y

    def __str__(self):
        return "{k: " + str(self.k) + ", b: " + str(self.b) + ", x: " + str(self.x) + ", y: " + str(self.y) + "}"

    def is_point_on_line(self, pointxy):
        """
        test if a point on a line
        """

        if self.k is not None and self.k * pointxy.x + self.b == pointxy.y:
            return True

        if self.x is not None and pointxy.x == self.x:
            return True

        if self.y is not None and pointxy.y == self.y:
            return True

        return False

    def get_x_from_y(self, y):
        if self.k is not None and self.k != 0:
            x = (y - self.b) / self.k
            return x

        if self.x is not None:
            return self.x

        if self.y is not None:
            raise Exception("line " + str(self) + " is parallels to x")

    def get_y_from_x(self, x):
        if self.k is not None and self.k != 0:
            return self.k * x + self.b

        if self.x is None:
            raise Exception('line ' + str(self) + ' is parallels to x')

        if self.y is None:
            return self.y

        raise Exception('unknown exception')

    @staticmethod
    def get_line_equation_from_two_points(point1, point2):
        """
        过两点求直线方程
        """

        dis_x = point1.x - point2.x
        dis_y = point1.y - point2.y

        if dis_x == dis_y and dis_x == 0:
            raise Exception("point1:" + str(point1) + " is equal point2: " + str(point2))

        if dis_x != 0 and dis_y != 0:
            k = dis_y / dis_x
            b = point1.y - k * point1.x
            return LineEquation(k, b)

        if 0 == dis_x:
            """
            parallels to y axis
            """
            return LineEquation(x=point1.x)

        if 0 == dis_y:
            """
            parallels to x axis
            """
            return LineEquation(y=point1.y)

        raise Exception("unknown exception")

    def get_foot_point_of_line(self, point):
        """
        get foot of a perpendicular
        :param point:
        :return:
        """
        if self.is_point_on_line(point):
            return point

        if self.k is not None:
            pass

        if self.x is not None:
            return PointXY(self.x, point.y)

        if self.y is not None:
            return PointXY(point.x, self.y)

        k_vertical = -self.k
        b_vertical = point.y - k_vertical * point.x

        x = (self.b - b_vertical)/(k_vertical - self.k)
        y = k_vertical * x + b_vertical

        return PointXY(x, y)

    def get_perpendicular_line(self, point):
        assert(point)

        if self.k is not None:
            k_vertical = -1 / self.k
            b_vertical = point.y - k_vertical * point.x

            return LineEquation(k_vertical, b_vertical)

        if self.x is not None:
            return LineEquation(y=point.y, b=point.y)

        if self.y is not None:
            return LineEquation(x=point.x)

        raise Exception('unknown exception')

    def get_parallel_lines_for_distance(self, distance):

        if self.k is not None:
            k_vertical = -1 / self.k
            b_vertical = self.b
            x_left = distance * math.sqrt(1 / (pow(k_vertical, 2) + 1))
            y_left = k_vertical * x_left + b_vertical
            # //y_left = self.k * x_left + b_left
            b_left = y_left - self.k * x_left

            x_right = -distance * math.sqrt(1 / (pow(k_vertical, 2) + 1))
            y_right = k_vertical * x_right + b_vertical
            # y_left = self.k * x_left + b_right
            b_right = y_right - self.k * x_right

            return [LineEquation(self.k, b_left), LineEquation(self.k, b_right)]

        if self.x is not None:
            return [LineEquation(x=self.x + distance), LineEquation(x=self.x - distance)]

        if self.y is not None:
            return [LineEquation(y=self.y + distance, b=self.y + distance), LineEquation(y=self.y - distance, b=self.y - distance)]

        raise Exception('unknown exception')


if __name__ == '__main__':

    line = LineEquation(9, 2, None, None)
    print(line)
    print('get_parallel_lines_for_distance')
    print(line.get_parallel_lines_for_distance(1))

    pointxy = PointXY(1, 11)
    print(line.is_point_on_line(pointxy))

    pointxy = PointXY(1, 10)
    print(line.is_point_on_line(pointxy))

    print(line.get_x_from_y(2))
    print(line.get_x_from_y(11))

    print(line.get_y_from_x(11))
    print(line.get_y_from_x(2))

    print(line.get_foot_point_of_line(PointXY(1,2)))

    line = LineEquation(1, 0)
    print(line)

    print(line.get_foot_point_of_line(PointXY(1,2)))
    print(line.get_foot_point_of_line(PointXY(1, 1)))

    print(LineEquation.get_line_equation_from_two_points(PointXY(1,1), PointXY(2,2)))
    print(LineEquation.get_line_equation_from_two_points(PointXY(1,1), PointXY(1,2)))
    print(LineEquation.get_line_equation_from_two_points(PointXY(2,2), PointXY(1,2)))

