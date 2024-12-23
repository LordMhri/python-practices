from collections import deque

class movingAverage:    
    def __init__(self,size):
        self.size = size
        self.list = deque()
        self.windowSum = 0.0
    
    def next(self,num):
        topLeft = 0
        if len(self.list) >= self.size:
            topLeft = self.list.popleft()
        self.windowSum -= topLeft

        self.list.append(num)
        self.windowSum += num
        if len(self.list) < self.size:
            return self.windowSum / len(self.list)
        return self.windowSum/self.size
        


m = movingAverage(3)
print(m.next(1))
print(m.next(10))
print(m.next(3))
print(m.list)
print(m.next(5))
print(m.list)
