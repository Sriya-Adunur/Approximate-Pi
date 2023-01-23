# Approximates pi using polygons.
# CSC 101, Project 1
# Given code, Summer '22
# TODO: Complete this program.

# NOTE: Initially, inscribe a square in a circle with radius 1. The square is
#       then a polygon whose 4 sides are each of length sqrt(2).
num_sides = 4
side_length = 2 ** 0.5
perimeter = num_sides * side_length
pi = perimeter / 2

# NOTE: Only round the approximation to the desired precision when printing. Do
#       not use the rounded value for subsequent iterations.
print("pi is approximately " + str(round(pi, 2)) + ".")
