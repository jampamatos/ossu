def lessThan4(aList):
    '''
    aList: a list of strings
    returns: all elements of list that contain fewer than 4 characters.
    '''

    returnList = []
    for el in aList:
        if len(el) < 4:
            returnList.append(el)
    
    return returnList