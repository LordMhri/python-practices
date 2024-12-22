class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        st = ''
        for i in range(len(s)):
            if s[i].isalnum():
                st += s[i].lower()
            
        left,right = 0,len(st)-1
        while left < right:
            if st[left] != st[right]:
                return False
            left += 1
            right -= 1
        
        return True