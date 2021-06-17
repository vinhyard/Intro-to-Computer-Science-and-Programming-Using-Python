#In this problem, you'll create a program that guesses a secret number!
#The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
# The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!
#Note: your program should use input to obtain the user's input! Be sure to handle the case when the user's input is not one of h, l, or c.
#When the user enters something invalid, you should print out a message to the user explaining you did not understand their input.


#At the start the highest the number could be is 100 and the lowest is 100.
chad = 100
doug = 0
answ = False

print('Please think of a number between 0 and 100!')


#Loop until we gues it correctly
while not answ:
    #Bisection search: guess the midpoint between our current high and low guesses
    guess = (chad + doug)//2
    print('Is your secret answer', guess, '?')
    palantir = input('Enter "h" to indicate too high. Enter "l" to indicate too low. Enter "c" to indicate I guessed correctly.')


    if palantir == 'c':
        answ = True


    elif palantir == 'h':
        chad = guess   
    
    elif palantir == 'l':
        doug = guess
    else: print('Sorry, I did not understand your input')
print('Game over. Your secret number was:', guess)