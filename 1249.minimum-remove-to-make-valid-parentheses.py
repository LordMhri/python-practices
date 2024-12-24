#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openCount = 0
        s = list(s)  
        for i in range(len(s)):
            if s[i] == '(':
                openCount += 1
            elif s[i] == ')':
                if openCount == 0:
                    s[i] = '*'
                else:
                    openCount -= 1
        
        openCount = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                if openCount == 0:
                    s[i] = '*'
                else:
                    openCount -= 1
            elif s[i] == ')':
                openCount += 1
        
        return ''.join([c for c in s if c != '*'])
        
# @lc code=end

