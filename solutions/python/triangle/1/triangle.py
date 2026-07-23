def greater_zero(a, b, c):
    return a > 0 and b > 0 and c > 0

def triangle_closable(a, b, c):
    return a+b >= c and a+c >= b and b+c >= a

def equilateral(sides): 
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if (not greater_zero(a,b,c)) or (not triangle_closable(a,b,c)):
        return False
        
    return a == b == c

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if (not greater_zero(a,b,c)) or (not triangle_closable(a,b,c)):
        return False
    
    return  a == b or a == c or b == c

def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if (not greater_zero(a,b,c)) or (not triangle_closable(a,b,c)):
        return False
    
    return a != b and b != c and c != a