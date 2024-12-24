#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#
from typing import List
# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        answer = []
        for char in s:
            if char == '(':
                if depth > 0:
                    answer.append(char)
                depth += 1
            elif char == ')':
                depth -= 1
                if depth > 0:
                    answer.append(char)
        
        return "".join(answer)

        
# @lc code=end

