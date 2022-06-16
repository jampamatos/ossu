import math

def polysum(n, s):
    '''
    n: an integer, represents the number of sides of a polygon
    s: an int or float, represent the lenght of each side of the polygon

    returns: the sum of the area and square of the perimeter of a n-side polygon, rounded up to 4 decimals.
    '''

    def perimeter(n, s):
        if n == 1:
            return s
        else:
            return s + (perimeter(n-1, s))

    area = (0.25 * n * s**2) / (math.tan(math.pi/n))
    per = perimeter(n,s)
    
    return round(area + per**2, 4)

print(polysum(48, 70)) # 12186714.6393