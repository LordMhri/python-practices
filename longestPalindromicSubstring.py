#O(n^3) solution
def longestPalindromicSubstring(s:str) -> str:
    ans = ''
    right = 0
    for left in range(len(s)):
        for right in range(left,len(s)):
            if isPalindrome(s[left:right+1]) and len(s[left:right+1]) > len(ans):
                ans = s[left:right+1]
    
    return ans

#O(n^2 solution)
def longestPalindrome(s: str) -> str:
    ans = ''
    ansLen = 0
    for i in range(len(s)):
        #odd length
        left,right = i,i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if ansLen < right - left + 1:
                ans = s[left:right+1]
                ansLen = right - left + 1
            left -= 1
            right += 1
        #even length
        left,right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if ansLen < right - left + 1:
                ans = s[left:right+1]
                ansLen = right - left + 1
            left -= 1
            right += 1

    return ans




def isPalindrome(s:str) -> bool:
    return s == s[::-1]


check = "ababnasd"
print(longestPalindromicSubstring(check))