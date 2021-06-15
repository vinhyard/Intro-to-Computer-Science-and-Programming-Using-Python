#In this problem, you'll create a program that guesses a secret number!
#The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
# The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!
#Note: your program should use input to obtain the user's input! Be sure to handle the case when the user's input is not one of h, l, or c.
#When the user enters something invalid, you should print out a message to the user explaining you did not understand their input.


high = 50
low = 50//2

i = 'l' 
u = 'h'

#high and low is for the range 0-100.

print('Please think of a number between 0 and 100!')
print('Is your secret number', high, '?')
chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
while i in chad:
    if i == 'l':
        high += low
        print('Is your secret number', high, '?')
        chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
        if chad == 'l':
            low = low//2
            high += low
            print('Is your secret number', high, '?')
            chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
            if chad == 'l':
                high += 6
                print('Is your secret number', high, '?')
                chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
                while chad == 'l':
                    high += 1
                    print('Is your secret number ', high, '?')
                    chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
                    
                
            else: break    
        else: break
        
    else:break

while u in chad:
    if u =='h':    
        high -= low
        print('Is your secret number', high, '?')
        chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
        if chad == 'h':
            low = low//2
            high -= low
            print('Is your secret number', high, '?')
            chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
            if chad == 'h':
                high += 6
                print('Is your secret number', high, '?')
                chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
                while chad == 'h':
                    high -= 1
                    print('Is your secret number ', high, '?')
                    chad = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')
            else: break
        else:break            
                   
    else:break
if chad == 'c': print('Game over. Your secret number was:', high)
else:print('Sorry, I did not understand your input.')    
    
       





