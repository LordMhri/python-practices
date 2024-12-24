#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
from collections import deque
# @lc code=start
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        self.q2.append(x)
        #append left is not allowed
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2,self.q1
    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

def test_MyStack():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2, "Test case 1 failed"
    assert stack.pop() == 2, "Test case 2 failed"
    assert stack.top() == 1, "Test case 3 failed"
    assert not stack.empty(), "Test case 4 failed"
    assert stack.pop() == 1, "Test case 5 failed"
    assert stack.empty(), "Test case 6 failed"
    print("All test cases passed!")

# Run the test case
test_MyStack()