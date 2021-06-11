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