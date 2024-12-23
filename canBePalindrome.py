from collections import Counter

def canBePalindrome(s:str) -> bool:
    count = Counter(s)
    oddCount = 0
    for key in count.keys():
        if count[key] % 2 != 0:
            oddCount += 1
        if oddCount > 1: 
            return False

    return True

print(canBePalindrome("racecarb"))




'''
racecar
r : 2
a : 2
e : 1  only one value with an odd count 
c:  2

'''