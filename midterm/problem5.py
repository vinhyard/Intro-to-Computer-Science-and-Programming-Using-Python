
#Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). 
# The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)

#This function takes in a dictionary and returns a list.











def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    sam = []
    chad = {}

    for i in list(aDict.keys()):
        if aDict[i] not in chad:
            chad[aDict[i]] = 1

        else:
            chad[aDict[i]] += 1

    for j in chad.keys():

        if chad[j] == 1:

            for t in aDict.keys():
                if aDict[t] == j:
                    sam.append(t)

   

    return sorted(sam)
