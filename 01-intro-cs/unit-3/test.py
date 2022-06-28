animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    num = 0

    for v in aDict.values():
        num += len(v)
    
    return num

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    biggest = ''
    biggest_len = 0

    for k in aDict:
        if len(aDict[k]) >= biggest_len:
            biggest = k
            biggest_len = len(aDict[k])
    
    return biggest


#print(how_many(animals))
print(biggest(animals))