def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns a list of keys in aDict that map to integer values that are unique.
    The list of keys you return should be sorted in increasing order. 
    If aDict does not contain any unique values, you should return an empty list.
    '''
    returnList = []
    values = [x for x in aDict.values()]
    unique = [x for x in values if values.count(x) == 1]
    for k,v in aDict.items():
        if v in unique:
            returnList.append(k)

    return sorted(returnList)

aDict = {'z': 1, 'b': 2, 'c': 2, 'a': 3, 'e': 2 }
print(uniqueValues(aDict))
print('---')
aDict = {'z': 1, 'b': 2, 'c': 3, 'a': 3, 'e': 2 }
print(uniqueValues(aDict))
print('---')
aDict = {'z': 1, 'b': 2 }
print(uniqueValues(aDict))
print('---')
aDict = {'z': 1, 'b': 1}
print(uniqueValues(aDict))
print('---')