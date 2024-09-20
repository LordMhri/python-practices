def romanToInt(s: str) -> int:
    mapping = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    ans = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and mapping[s[i]] < mapping[s[i+1]]:
            ans += mapping[s[i+1]] - mapping[s[i]] 
            i+=2
        else:
            ans += mapping[s[i]]
            i+=1
    
    return ans

s = "MCMXCIV"
print(romanToInt(s))
    
'''
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

1000 + -100 + 1000 + -10 + 50 + -1 + 5 = 1994
 M        C    M      X    C     I   V
 
 check if the next one is bigger than the current one if so subtract the first one from the sum
 '''