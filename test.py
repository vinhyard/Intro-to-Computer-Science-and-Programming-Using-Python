high = 50
high1 = 50/2




print('Please think of a number between 0 and 100!')
print('Is your secret number', high, '?') 
chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
while high < 100:
    if chad == 'h':
        high //=2
        print(high)
        print('Is your secret number', high, '?') 
        chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
        if chad == 'h':
            high //=2
            print(high)
            print('Is your secret number', high, '?')
            chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
            if chad == 'h':
                high //=2
                print('Is your secret number', high, '?')
                chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
                if chad == 'h':
                    high //=2
                    print('Is your secret number', high, '?')
                    chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
                    if chad == 'h':
                        high -= 1
                        print('Is your secret number', high, '?')
                    if chad == 'l':
                        print('Is your secret number')
                        high += 1
                        print('Is your secret number', high, '?')
                elif chad == 'l':
                    high += (high//2)
            else: 
                chad == 'l'
                high += (high//2)
                print('Is your secret number', high, '?')
        elif chad == 'l':
            high += (high//2)
            print(high)
            print('Is your secret number', high, '?') 
    elif chad == 'l':
        high += high1
        print(high)  
    elif chad == 'c':
        print('Game Over. Your secret number was:', high)
        break
    else: 
        print('sorry')
        
else:

    

    print('Sorry, I did not understand your input')
