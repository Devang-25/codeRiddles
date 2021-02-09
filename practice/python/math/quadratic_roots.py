# from math import sqrt

# handles imaginary numbers (sqrt(negative))
from cmath import sqrt


def quadraticRoots(a, b, c):
    """
    ax2 + bx + c

    print to see this equation:

    roots = (-b +- √(b2 - 4ac))
            ----------------------
                     2a

    """
    if a != 0:
        root_1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        root_2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        print(f"Solving for Quadratic: {a}x2 + {b}x + {c}")
        print(root_1, root_2)
    else:
        print(f"Linear equation {b}.x+{c} since a = {a}")
        print("Single root: ", -c / b)


a, b, c = [int(i) for i in input("Enter with space - a, b, c: ").split()]

quadraticRoots(a, b, c)
