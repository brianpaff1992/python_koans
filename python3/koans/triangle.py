#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    ensure_valid_dimensions(a, b, c)
    if a == b and b == c:
        return 'equilateral'
    elif a == b or b == c or a == c:
        return 'isosceles'
    elif a != b and b != c and a != c:
        return 'scalene'


def ensure_valid_dimensions(a, b, c):
    c_doesnt_exist_in_human_dimension = a <= 0 or b <= 0 or c <= 0
    c_sides_do_not_add_up_correctly = a + b < c or a + c < b
    if c_doesnt_exist_in_human_dimension or c_sides_do_not_add_up_correctly:
        raise TriangleError()


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
