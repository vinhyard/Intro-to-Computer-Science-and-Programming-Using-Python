#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. or example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5



s = 'massachusetts of institute of technology'
count = 0
for char in s:
    if char == 'a': 
        count = count + 1
    elif char == 'e':
        count = count + 1
    elif char == 'i':
        count = count + 1
    elif char == 'o': 
        count = count + 1
    elif char == 'u':
        count = count + 1
    else: continue     
print('Number of Vowels:',count)
