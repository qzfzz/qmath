#!/bin/env python3
# coding:utf-8
# author bruce

from qmath.geometry.c2d.pointxy import PointXY
from qmath.geometry.c2d.lineequation import LineEquation


class LineSegment:

    """
    line equation
    """
    line_equation = None
    point1 = None
    point2 = None

    def __init__(self, point1, point2 ):
        self.point1 = point1
        self.point2 = point2

        self.line_equation = LineEquation.get_line_equation_from_two_points(point1, point2)

    def __str__(self):
        return "{line_equation: " + str(self.line_equation) + ", point1: " + str(self.point1) + ", point2: " + str(self.point2) + "}"

    def is_point_in_line_segment(self, pointxy):
        """
        test if a point on a line segment
        """
        if not self.line_equation.is_point_on_line(pointxy):
            return False

        left_x = self.point2.x if self.point2.x < self.point1.x else self.point1.x
        right_x = self.point2.x if self.point2.x > self.point1.x else self.point1.x

        bottom_y = self.point2.y if self.point2.y < self.point1.y else self.point1.y
        top_y = self.point2.y if self.point2.y > self.point1.y else self.point1.y

        if pointxy.x >= left_x and pointxy.x <= right_x and pointxy.y >= bottom_y and pointxy.y <= top_y:
            return True

        return False


