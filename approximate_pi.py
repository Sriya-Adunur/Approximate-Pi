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

iterations = int(input("How many iterations should be performed? "))
decimals = int(input("How many decimal places should be reported? "))

if iterations < 4:
    print("Error: Cannot perform < 4 iterations.")

elif decimals > 7: 
    print("Warning: Cannot report > 7 decimal places.")
    print("pi is approximately " + str(round(pi, 7)) + ".")

    for i in range(iterations - 1):
        side_length = (((side_length ** 2)/4 + ((1 - ((1 - ((side_length ** 2)/4)) ** .5)) ** 2)) ** .5)
        num_sides = num_sides * 2
        new_perimeter = num_sides * side_length
        new_pi = new_perimeter/2
        print("pi is approximately " + str(round(new_pi, 7)) + ".")

elif decimals < 0:
    print("Warning: Cannot report < 0 decimal places.")
    print("pi is approximately " + str(round(pi, 0)) + ".")   

    for i in range(iterations - 1):
        side_length = (((side_length ** 2)/4 + ((1 - ((1 - ((side_length ** 2)/4)) ** .5)) ** 2)) ** .5)
        num_sides = num_sides * 2
        new_perimeter = num_sides * side_length
        new_pi = new_perimeter/2
        print("pi is approximately " + str(round(new_pi, 0)) + ".")

else:
    print("pi is approximately " + str(round(pi, decimals)) + ".")
    
    for i in range(iterations - 1):
        side_length = (((side_length ** 2)/4 + ((1 - ((1 - ((side_length ** 2)/4)) ** .5)) ** 2)) ** .5)
        num_sides = num_sides * 2
        new_perimeter = num_sides * side_length
        new_pi = new_perimeter/2
        print("pi is approximately " + str(round(new_pi, decimals)) + ".")
