"""Module allowing identification of types of triangles based on a tuple of sides"""

def triangle(sides):
    sorted_sides = sorted(sides)
    if sorted_sides[0] > 0 and sorted_sides[0] + sorted_sides[1] >= sorted_sides[2]:
        return True
    return False

def equilateral(sides):
    if triangle(sides) and sides[0] == sides[1] == sides[2]:
        return True
    return False

def isosceles(sides):
    if triangle(sides) and len(set(sides)) <= 2: #Equilateral counts as isosceles
        return True
    return False


def scalene(sides):
    if triangle(sides) and len(set(sides)) == 3:
        return True
    return False
