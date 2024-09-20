def mergeAlternately(word1: str, word2: str) -> str:
    #is basically mergeSort with a few things changed
    length1 = len(word1)
    length2 = len(word2)
    ans = ''
    
    i = 0
    j = 0
    while(i < length1 and j < length2):
        ans += word1[i]
        ans += word2[i]
        i += 1
        j += 1
    
    while i < length1:
        ans += word1[i]
        i += 1
    while j < length2:
        ans += word2[j]
        j += 1
        
    return ans
 
word1 = "ab"
word2 = "pqrs"
print(mergeAlternately(word1,word2))
        
    