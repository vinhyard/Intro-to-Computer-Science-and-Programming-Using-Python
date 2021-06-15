#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2

s = 'azcbobobegghakl'
count = 0
for i in range(len(s)):
    if s[i:i + 3] == 'b' + 'o' + 'b':
        count = count + 1
    else: continue
print('Number of times bob occured is:', count)        
