#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                temp = ''
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop() #this is popping the "[" character
                #i know that before a [ character we always have a digit character
                #and the digit value can be from 1-300 so we're not looking for a single 
                #digit we're looking until we find a non digit in the stack
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * temp)
        
        return "".join(stack)

        
# @lc code=end

