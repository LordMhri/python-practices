from collections import Counter,deque
class FirstUnique:
    def __init__(self,nums):
        self.q = deque()
        self.mapp = Counter()

        for num in nums:
            self.add(num)


    def add(self,num):
        
        if self.mapp[num] == 0:
            self.q.append(num)
        self.mapp[num] += 1

        
    
    def showFirstUnique(self):
        while self.q and self.mapp[self.q[0]] > 1:
            self.q.popleft()
        
        if self.q:
            return self.q[0]
        else:
            return  -1
            
check = FirstUnique([2,7,3,1,2,1])
print(check.q)
print(check.showFirstUnique())

print(check.showFirstUnique())

print(check.showFirstUnique())


print(check.showFirstUnique())
