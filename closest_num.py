def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here

    power = 0
    product = 1
    diff = num - product
    prev_diff = num
  
    while diff < prev_diff:
        product *= base
        power += 1
        prev_diff = diff
        diff = abs(num - product)
    return power-1
