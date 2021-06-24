#Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. 
# This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.
#Example Usage:
#>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#>>> print(getAvailableLetters(lettersGuessed))
#abcdfghjlmnoqtuvwxyz
#Note that this function should return the letters in alphabetical order, as in the example above.
#For this function, you may assume that all the letters in lettersGuessed are lowercase.
#Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters:
#>>> import string
#>>> print(string.ascii_lowercase)
#abcdefghijklmnopqrstuvwxyz
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    nio = string.ascii_lowercase
    for i in range(len(string.ascii_lowercase)):
      if string.ascii_lowercase[i] in lettersGuessed:
        nio = nio.replace(string.ascii_lowercase[i], '')
    return nio
           
    
print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))