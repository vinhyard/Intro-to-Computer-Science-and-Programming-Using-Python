#Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic .ax^2 + bx + c
#This function takes in four numbers and returns a single number.



def evalQuadratic(a, b, c, x):
    nio = a * (x**2) + b * x + c

    '''
a, b, c, x: int or float

    '''
    return nio

print(evalQuadratic(1, 4, 5, 8))