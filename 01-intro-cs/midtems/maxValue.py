def max_val(t): 
    """ t, tuple or list
    Each element of t is either an int, a tuple, or a list
    No tuple or list is empty
    Returns the maximum int in t or (recursively) in an element of t """ 

    flatlist = []
    for e in t:
        if type(e) == int:
            flatlist.append(e)
        else:
            flatlist.append(max_val(e))
    
    return max(flatlist)

print(max_val((5, (1,2), [[1],[2]])))
print(max_val((5,1,2,1,2)))