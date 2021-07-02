#Write a simple procedure, myLog(x, b), that computes the logarithm of a number x relative to a base b. 
# For example, if x = 16 and b = 2, then the result is 4 - because  24=16 . If x = 15 and b = 3, then the result is 2 - because  32  is the largest power of 3 less than 15.

#In other words, myLog should return the largest power of b such that b to that power is still less than or equal to x.

#x and b are both positive integers; b is an integer greater than or equal to 2. Your function should return an integer answer.






def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here

    n = 0
    chad = b
    while chad**n <= x:

        n += 1

    n -= 1
    return n

print(myLog(15, 3))