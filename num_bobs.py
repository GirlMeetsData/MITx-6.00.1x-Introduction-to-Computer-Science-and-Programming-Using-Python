bobs_count = 0
target = 'bob'
for i in range(len(s)):
 if s[i:i+len(target)] == target:
  bobs_count +=1 
  
print(bobs_count)
