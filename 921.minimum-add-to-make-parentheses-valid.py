#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#
from typing import List
# @lc code=start

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openCount = 0
        closeCount = 0
        for char in s:
            if char == '(':
                openCount += 1
            else:
                if openCount > 0:
                    openCount -= 1
                else:
                    closeCount += 1
        
        return openCount + closeCount
# @lc code=end


def test_minAddToMakeValid():
    solution = Solution()

    # Test case 1: Balanced parentheses
    assert solution.minAddToMakeValid("()") == 0

    # Test case 2: Single opening parenthesis
    assert solution.minAddToMakeValid("(") == 1

    # Test case 3: Single closing parenthesis
    assert solution.minAddToMakeValid(")") == 1

    # Test case 4: Multiple unbalanced parentheses
    assert solution.minAddToMakeValid("(((") == 3
    assert solution.minAddToMakeValid(")))") == 3

    # Test case 5: Mixed unbalanced parentheses
    assert solution.minAddToMakeValid("(()") == 1
    assert solution.minAddToMakeValid("())") == 1
    assert solution.minAddToMakeValid("((())") == 1
    assert solution.minAddToMakeValid("())(") == 2

    # Test case 6: Complex unbalanced parentheses
    assert solution.minAddToMakeValid("((())())") == 0
    assert solution.minAddToMakeValid("((())(()") == 2
    assert solution.minAddToMakeValid(")()(") == 2

    print("All test cases pass")
test_minAddToMakeValid()