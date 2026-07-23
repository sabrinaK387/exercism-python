def greater_zero(a, b, c):
    """Tests if any side is > 0"""
    return a > 0 and b > 0 and c > 0

def triangle_closable(a, b, c):
    """Tests if the triangle sides are too short to close the triangle"""
    return a+b >= c and a+c >= b and b+c >= a

def equilateral(sides): 
    """Tests if a triangle has equal long sides"""
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if (not greater_zero(a,b,c)) or (not triangle_closable(a,b,c)):
        return False
        
    return a == b == c

def isosceles(sides):
    """Tests if a triangle has 2 equal long sides"""
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if (not greater_zero(a,b,c)) or (not triangle_closable(a,b,c)):
        return False
    
    return  a == b or a == c or b == c

def scalene(sides):
    """Tests if a triangle has none equal long sides"""
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if (not greater_zero(a,b,c)) or (not triangle_closable(a,b,c)):
        return False
    
    return a != b and b != c and c != a