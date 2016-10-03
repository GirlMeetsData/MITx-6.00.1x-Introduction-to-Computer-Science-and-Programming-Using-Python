def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    newL = L[::-1]
    newestL = []

    for l in newL:
        newestL.append(l[::-1])
        L[:]=newestL
