from collections import Counter

def canBePalindrome(s:str) -> bool:
    count = Counter(s)
    oddCount = 0
    for i in range(len(s)):
        if count[s[i]] % 2 != 0:
            oddCount += 1
        if oddCount > 1: 
            return False
    print(count)
    return True

print(canBePalindrome("racecar"))




'''
racecar
r : 2
a : 2
e : 1  only one value with an odd count 
c:  2

'''