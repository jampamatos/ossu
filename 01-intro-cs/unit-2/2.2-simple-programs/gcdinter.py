def smallest (a,b):
    '''
    a, b: positive integers
    returns: a positive integer, the smallest of the two arguments
    '''
    if a < b:
        return a 
    else:
        return b


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    test = smallest(a,b)
    
    while test > 0:
        if test == 1:
            return test
        elif a % test == 0 and b % test ==0:
            return test
        else:
            test -=1


print(gcdIter(2, 12))
print(gcdIter(6, 12))
print(gcdIter(9, 12))
print(gcdIter(17, 12))

# 2, 6, 3, 1