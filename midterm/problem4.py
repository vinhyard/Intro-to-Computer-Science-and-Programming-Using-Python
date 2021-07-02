#Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters.
#  For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]

#This function takes in a list of strings and returns a list of strings. Your function should not modify aList.










def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here

    bob = []
    
    for i in range(len(aList)):
        if len(aList[i]) < 4:
            bob.append(aList[i])
        else:continue
    return bob
    
print(lessThan4(["apple", "cat", "dog", "banana"])) 
