def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    
    result = 1
    for _ in range(exp):
        result *= base
    return result
    
 # base should mutliple itself by exp times

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        result = base*recurPower(base,exp-1)
        return result

def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    
    return square(x) * square(x)


def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    return x%2!=0

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    if b == 0:
      return a
    else:
      return gcdRecur(b, a % b)
