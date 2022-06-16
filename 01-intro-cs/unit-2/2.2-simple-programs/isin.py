def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    elif len (aStr) == 1 and char == aStr:
        return True
    elif len (aStr) == 1 and char != aStr:
        return False
    else:
        testChar = aStr[len(aStr)//2]
        if testChar == char:
            return True
        elif testChar > char:
            return isIn(char, aStr[0:len(aStr)//2])
        elif testChar < char:
            return isIn(char, aStr[len(aStr)//2+1:])

#print(isIn('a', '')) #False
#print(isIn('l', 'loptww')) #True
print(isIn('r', 'iiiloqqruwx')) #True
print(isIn('x', 'bcegjjlmrrty')) #False
print(isIn('a', 'ei')) #False
print(isIn('m', 'aacdfgijlnnpqssuxz')) #False
print(isIn('f', 'bdghkmrsz')) #False
print(isIn('r', 'afqqrtvxy')) #True
print(isIn('k', 'affhikmmnprtyy'))