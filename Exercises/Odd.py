#Write a Python function, odd, that takes in one number and returns True when the number is odd and False otherwise.

#You should use the % (mod) operator, not if.

#This function takes in one number and returns a boolean.


def odd(x):
    dad = False
    if x%2 != 0:
        dad = True
        
    return dad
    

print(odd(5))