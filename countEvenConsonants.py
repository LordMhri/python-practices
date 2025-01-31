def countEvenConsonant(s,k):
    vowel = {"a","e","i","o","u"}
    ans = 0
    curr = 0
    left = 0
    for right in range(len(s)):
        if s[right] not in vowel:
            curr += 1
        if right-left+1 == k:
            if curr % 2 == 0:
                ans += 1
            if s[left] not in vowel:
                curr -= 1
            
            left += 1
    
    return ans

print(countEvenConsonant("aabbcc",2))
'''
Input: s = "abcde", m = 3
Output: 2
Explanation: The substrings of length 3 are "abc", 
"bcd", "cde". "abc" and "cde" have an even number of consonants.

a,b,c

b:1
c:1

'''