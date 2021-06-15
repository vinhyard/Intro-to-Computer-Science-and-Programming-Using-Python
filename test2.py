high = 50
high1 = 50/2




print('Please think of a number between 0 and 100!')
print('Is your secret number', high, '?') 
while high <= 50:
    chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
    if chad == 'h':
        high //=2
        print('Is your secret number', high, '?') 
        while 0 <= high <= 5 or 19 <= high <= 23  :
            chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
            if chad == 'h':
                high -= 1
                print('Is your secret number', high, '?')
            elif chad == 'l':
                high += 1
                print('Is your secret number', high, '?')
            elif chad == 'c':
                print('Game over. Your secret number was:', high) 
    elif chad == 'l':  
        if high == 18:
  
            if chad == 'l':
                high += (high//6)
                print('Is your secret number', high, '?')
            elif chad == 'h':
                high -= (high//6)   
                print('Is your secret number', high, '?')  
        while 7 <= high < 12 or 15 <= high <= 17 or 19 <= high <= 24:
            
            chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
            if chad == 'h':
                high -= 1
                print('Is your secret number', high, '?')
            elif chad == 'l':
                high += 1
                print('Is your secret number', high, '?')
            elif chad == 'c':
                print('Game over. Your secret number was:', high)
       
        
        high += (high//2)
        print('Is your secret number', high, '?')
        
    elif chad == 'c':
        break
    
print('Game over. Your secret number was: ', high,)