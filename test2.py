high = 50
high1 = 50/2




print('Please think of a number between 0 and 100!')
print('Is your secret number', high, '?') 
chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
while high < 100:
    if chad == 'h':
        high //=2
        print('Is your secret number', high, '?') 
        chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
    elif chad == 'l':
        high += (high//2)
        print('Is your secret number', high, '?')
        chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
    elif chad == 'c':
        break
    
print('Game over. Your secret number was: ', high,)