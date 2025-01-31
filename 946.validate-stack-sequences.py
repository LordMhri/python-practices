#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#
from typing import List
# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        idx = 0
        for char in pushed:
            stack.append(char)
            while stack and stack[-1] == popped[idx]:
                stack.pop()
                idx += 1
        
        return not stack

# @lc code=end

