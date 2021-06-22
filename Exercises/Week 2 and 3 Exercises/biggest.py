#ESTIMATED TIME TO COMPLETE: 7 minutes

#Consider the following sequence of expressions:

#animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

#animals['d'] = ['donkey']
#animals['d'].append('dog')
#animals['d'].append('dingo')
#We want to write some simple procedures that work on dictionaries to return information.

#This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it.
#  If there is more than one such entry, return any one of the matching keys.

#Example usage:

#>>> biggest(animals)
#'d'
#If there are no values in the dictionary, biggest should return None.


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def biggest(aDict):

    biggest = []
    if aDict == False:
        return 'None'
    else:
        for num in aDict.items():
            if len(num) >= len(biggest):
                biggest = num[0]
        return biggest

    
print(biggest(animals))
