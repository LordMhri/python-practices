class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.minStack = []
        
    def push(self,val:int) -> None:
        self.stack.append(val)
        
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
    
    
    def pop(self) -> None:
        val = self.stack.pop()
        
        if val == self.minStack[-1]:
            self.minStack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]

#two stacks used for efficent o(1) retreivals at every method
'''
    minStack holds the current minimum values of our stack and stack is our main stack
    
    at push method we push the value onto the main stack and check if our minstack is empty
    if minstack is empty then whatever value we have becomes the smallest and biggest value
    simultaneously but if our minstack is not empty we check if the last value in it is bigger
    than the value we have on hand if not add it to the minStack
    
    at the pop method we pop out the top value and also check if it is the smallest value
    we have by checking if it is the same as the minStack[-1] if so pop out else do nothing
    
    the other methods are staright forward   


'''