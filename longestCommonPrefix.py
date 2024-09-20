def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]
    #the answer is at least as big as the shortest string
    #and sorting would take cost O(nlogn) at the least
    #so taking the first string is a good start
    
    for i in range(1,len(strs)): #first string taken so ignore and start from the next index
        #check if current string starts with prefix
        while not strs[i].startswith(prefix):
            #shorten prefix until current string starts with prefix
            #if shortened until it no longer exists then return the empty string
            prefix = prefix[:-1]
            if not prefix:
                return ""
            
    return prefix
     
strs = ["flower","flow","flight"]

print(longestCommonPrefix(strs))   
        
'''
Input: strs = ["flower","flow","flight"]
Output: "fl"

'''
        