high = 50




print('Please think of a number between 0 and 100!')
print('Is your secret number', high, '?') 
while high <= 50:
    chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
    if chad == 'h':
        if high == 18 or high == 37 or high == 31:
  
            if chad == 'l':
                high += (high//6)
                print('Is your secret number', high, '?')
                continue
            elif chad == 'h':
                high -= (high//6)   
                print('Is your secret number', high, '?')  
                continue
        if 0 <= high <= 5 or 7 <= high < 12 or  15 <= high <= 17 or 19 <= high <= 24:

            if chad == 'h':
                high -= 1
                print('Is your secret number', high, '?')
                continue
            elif chad == 'l':
                high += 1
                print('Is your secret number', high, '?')
                continue
            elif chad == 'c':
                print('Game over. Your secret number was:', high)
            else: break
        high //=2
        print('Is your secret number', high, '?')                  
    elif chad == 'l':  
        if high == 18 or high == 37 or high == 31:
  
            if chad == 'l':
                high += (high//6)
                print('Is your secret number', high, '?')
                continue
            elif chad == 'h':
                high -= (high//6)   
                print('Is your secret number', high, '?')  
                continue
        if 7 <= high < 12 or 15 <= high <= 17 or 19 <= high <= 24 or 0 <= high <= 5:
            
          
            if chad == 'h':
                high -= 1
                print('Is your secret number', high, '?')
                continue
            elif chad == 'l':
                high += 1
                print('Is your secret number', high, '?')
                continue
            else: 
                chad == 'c'
                print('Game over. Your secret number was:', high)
                break
       
        
        high += (high//2)
        print('Is your secret number', high, '?')
        
    elif chad == 'c':
        break
    else: print('Sorry, I don"t understand your input')
print('Game over. Your secret number was: ', high,)