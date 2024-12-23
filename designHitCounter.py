from collections import deque

class hitCounter:

    def __init__(self):
        self.list = []

    def hit(self,num):
        if not self.list or self.list and self.list[-1][0] != num:
            self.list.append([num,1])
        else:
            self.list[-1][1] += 1

    def getHits(self,num):
        _sum = 0
        length = len(self.list)
        i = length
        while i > 0 and self.list[i-1][0] > num-300:
            _sum += self.list[i-1][1]
            i -= 1
        return _sum

h = hitCounter()
for i in range(7):
    h.hit(i+1)

h.hit(8)
h.hit(8)
h.hit(8)
h.hit(8)
h.hit(8)

print(h.list)
print(h.getHits(301))

class hitCounterOptimized:

    def __init__(self):
        self.q = deque(300) #stores only the last 300 seconds
    
    def hit(self,num):
        if not self.q or self.q and self.q[-1][0]!= num: #if the queue is empty or we haven't encountered num yet
            self.q.append([num,1]) #create a new one
        else:
            self.q[-1][1] += 1
        
        #this ensures every element in our queue is not older than the most recent item by at least 300
        while self.q and self.q[0][0] <= num - 300:#if we found values older than 300 remove them from the queue
            self.q.popleft()

    
    def getHits(self,num):
        _sum = 0
        
        for val,count in self.q:
            if val > num - 300:
                _sum += count
        return _sum
