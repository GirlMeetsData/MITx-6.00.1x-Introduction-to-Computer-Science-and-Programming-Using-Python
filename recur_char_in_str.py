def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1 and char == aStr:
        return True
    elif len(aStr) == 1 and char != aStr:
        return False
        
        
    half = len(aStr)//2
    middle = aStr[half]
    
    if middle == char:
        return True
    elif middle < char:
        aStr = aStr[half:]
        return isIn(char, aStr)
    else:
        aStr = aStr[:half]
        return isIn(char, aStr)
