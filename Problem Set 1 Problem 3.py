#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print Longest substring in alphabetical order is: beggh
s = 'azcbobobegghakl'
alpha = ''
beta = ''
for i in range(len(s)):
    if s[i] <= s[i + 1]:
        beta += s[i] 
    else: print(beta)               

