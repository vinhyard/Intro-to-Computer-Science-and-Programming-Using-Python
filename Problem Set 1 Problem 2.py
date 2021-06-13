s = 'azcbobobegghakl'
count = 0
for i in range(len(s)):
    if s[i:i + 3] == 'b' + 'o' + 'b':
        count = count + 1
    else: continue
print('Number of times bob occured is:', count)        
