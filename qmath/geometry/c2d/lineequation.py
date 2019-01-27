#!/bin/env python3
# coding:utf-8
# author bruce


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

    def is_point_online(self, pointxy):
        """
        test if a point on a line
        """

        if self.k is not None and self.k * pointxy.x + self.b == pointxy.y:
            return True
        else:
            return False

    def get_x_from_y(self, y):
        if self.k is not None and self.k != 0:
            x = (self.y - self.b) / self.k
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
        dis_y = point2.y - point2.y

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


if __name__ == '__main__':

    line = LineEquation(9, 2, None, None)
    print(line)



