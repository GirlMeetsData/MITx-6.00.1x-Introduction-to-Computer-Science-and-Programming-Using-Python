def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    multIndex = 0
    result = []
    while multIndex < len(listA):
        result.append(listA[multIndex] * listB[multIndex])
        multIndex += 1
    return sum(result)
