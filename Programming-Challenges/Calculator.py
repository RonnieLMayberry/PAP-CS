'''
Created on December 2, 2014

@author: mayberryr
'''
# Function Calculator
# Calculates certain equations using different selectable functions.
# Ronnie Mayberry
# Tuesday, December 2, 2014

import math
        
choice = None
while choice != "0":

    print(
    """
    --------------------Calculators--------------------

                    0 - Exit
                    1 - Area of a Rectangle
                    2 - Area of a Triangle
                    3 - Area of a Trapezoid
                    4 - Quadratic Equation
                    5 - Area of a Circle
                    6 - Perimeter of a Rectangle
                    7 - Perimeter of a Square
                    8 - What's the Grade?
                    9 - Square Root
                    10 - Hypotenuse 
                    
    """
    )

    choice = input("Choice: ")

# Exit

    if choice == "0":
        print("Good-bye.")

# Area of a Rectangle

    if choice == "1":
        length = 0
        width = 0

        def rect(length, width):
            return length * width

        length = int(input("What is the length?"))
        width = int(input("What is the width?"))

        tot = rect(length, width)

        print("The length of the rectangle is ", length, ", the width of the rectangle is ", width, ", and the area \
of the rectangle is ", tot, ".")

# Area of a Triangle

    if choice == "2":
        base = 0
        width = 0

        def tri(base, height):
            return base * height

        base = int(input("What is the base of the triangle? "))
        height = int(input("What is the height of the triangle? "))

        area = tri(base, height) * .5

        print("The base of the triangle is ", base, ", the height of the triangle \
is ", height, ", and the area of the triangle is ", area, ".")

# Area of a Trapezoid

    if choice == "3":
        base_1 = 0
        base_2 = 0
        height = 0

        def trap(base_1, base_2, height):
            return base_1 * base_2 * height

        base_1 = int(input("What is the first base of the trapezoid? "))
        base_2 = int(input("What is the second base of the trapezoid? "))
        height = int(input("What is the height of the trapezoid? "))

        area = trap(base_1, base_2, height) * .5

        print("The first base of the trapezoid is ", base_1, ", the second base of the trapezoid \
is ", base_2, ", the height of the trapezoid is ", height, ", and the area of the trapezoid is ", area, ".")

# Quadratic Equation

    if choice == "4":
        def quadd(a, b, c):
            disc = (b**2) - (4 * a * c)
            return disc

        def quad1(a, b, disc):
            tot1 = (-b + disc) / (2 * a)
            return tot1

        a = int(input("What is 'a'? "))
        b = int(input("What is 'b'? "))
        c = int(input("What is 'c'? "))

        disc = quadd(a, b, c)
        print("The discrimnant is ", disc, ".")

        if disc <0:
            print("The solution is negative. Try again.")
            
        else:
            disc = disc**.5
            
            tot1 = quad1(a, b, disc)

            tot2 = quad1(a, b, -disc)

            print("The solutions are :", tot1, "and ", tot2, ".")

# Area of a Circle

    if choice == "5":
        def circ(radius):
            return math.pi * radius**2

        radius = int(input("What is the radius? "))
        area = circ(radius)

        print("The area of the circle is ", area, ".")

# Perimeter of a Rectangle

    if choice == "6":
        def rectper(a, b):
            return (a + b) * 2

        a = int(input("What is the length of the rectangle? "))
        b = int(input("What is the width of the rectangle? "))
        perimeter = rectper(a, b)

        print("The perimeter of the rectangle is: ", perimeter, "\.")

# Perimeter of a Square

    if choice == "7":
        def sqper(a):
            return a * 2

        a = int(input("What is the length of one side on the square? "))
        perimeter = sqper(a)

        print("The perimeter of the rectangle is: ", perimeter, "\.")

# What's the Grade?

    if choice == "8":
        def grad(grade):
            if grade == 100:
                return "A+"
            elif grade >= 90:
                return "A"
            elif grade >= 80:
                return "B"
            elif grade >= 70:
                return "C"
            else:
                return "F"

        grade = int(input("What is your grade? "))
        letter = grad(grade)
        print("Your letter grade is: ", letter, ".")
        
# Square Root

    if choice == "9":
        def squ(numb):
            return math.sqrt(numb)
        numb = int(input("What number do you want to square root? "))
        print("The square root of", numb, "is: ", squ(numb), ".")

# Hypotenuse

    if choice == "10":
        def pyth(a, b):
            return ((a * a + b * b) ** (.5))

        a = int(input("What is the length of a? "))
        b = int(input("What is the length of b? "))
        c = pyth(a, b)

        print("The hypotenuse is ", c, ".")
