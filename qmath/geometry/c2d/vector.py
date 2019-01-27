#!/bin/env python3
# coding:utf-8
# author bruce

from qgeo.twod.lineequation import LineEquation


class Vector:

    """
    we define a vector like this
                    left side(-1)
    begin_point -----------------> end_point
                    right side(1)
    """

    LEFT_SIDE = -1
    RIGHT_SIDE = 1

    begin_point = None
    end_point = None

    # line equation for vector
    line_equation = None

    def __init__(self, begin_point, end_point):
        self.begin_point = begin_point
        self.end_point = end_point

        line_equation = LineEquation.get_line_equation_from_two_points(begin_point, end_point)
        self.line_equation = line_equation

    @staticmethod
    def is_point_on_vector(point, vector):
        """
        point one line
        """
        return False

    @staticmethod
    def is_point_in_vector(point, vector):
        """
        point in vector
        :param point:
        :return:
        """
        return False

    @staticmethod
    def get_point_on_side_of_vector(point, vector):
        """
        point on which side of vector
        :param point:
        :return:
        """
        return Vector.LEFT_SIDE

