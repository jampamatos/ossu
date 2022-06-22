# Your Code Here
# [2, -3, 9, -8]

testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def plusOne(a):
    if a > 0:
        return a + 1
    else:
        return a - 1

applyToEach(testList,plusOne)