#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print to 
# 'Longest substring in alphabetical order is: abc
#Note: This problem may be challenging. We encourage you to work smart. 
# If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. 
# If you have time, come back to this problem after you've had a break and cleared your head
s = 'abcbcd'

alpha = ''
beta = s[0]
for i in range(len(s)):
    if s[i] >= s[i - 1]:
        beta += s[i]  
        if len(beta) > len(alpha):
            alpha = beta         
    else: beta = s[i]
print(alpha)           

