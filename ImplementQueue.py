class Queue:
    def __init__(self):
        self.st1 = []
        self.st2 = []
    
    def pop(self):
        if not self.st2: #if the second stack is empty
            while self.st1:
                self.st1.append(self.st1.pop())
        return self.st2.pop()

    def peek(self):
        if not self.st2:
            while self.st1:
                self.st1.append(self.st1.pop())
        return self.st2[-1]

    def isEmpty(self):
        return not self.st1 and self.st2
