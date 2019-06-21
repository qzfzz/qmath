#!/bin/env python3
# coding:utf-8
# author bruce

from qmath.geometry.c2d.lineequation import *


class LineEquationGeneral:
    """
    general form line equation
    """
    A = None
    B = None
    C = None

    def __init__(self, A=None, B=None, C=None):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return "{Ax + By + C = 0}: " + str(self.A) + "X + " + str(self.B) + "Y + " + str(self.C) + " = 0"

    def get_slope_intercept_form_line_equation(self):
        if self.A is None or self.A == 0:
            # By+C = 0
            # y = -C/B
            return LineEquation(None, -self.C / self.B, None, -self.C / self.B)

        if self.B is None or self.B == 0:
            # Ax + C = 0
            return LineEquation(None, None, -self.C / self.A, None)

        # Ax + By + C = 0
        # By = -Ax - C => y = -Ax/B - C/B
        return LineEquation(-self.A/self.B, -self.C/self.B, None, None)


if __name__ == '__main__':
    lineGeneral = LineEquationGeneral(4, 3, -12)
    bx = lineGeneral.get_slope_intercept_form_line_equation()
    print(bx)
