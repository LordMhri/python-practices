class MRUQueue:

    def __init__(self,cap):
        self.cap = cap
        self.list = [i + 1 for i in range(cap)]
    #this fetch is an O(n) call and can be further optimized
    def fetch(self,k):
        k -= 1
        while k < len(self.list) - 1:
            self.list[k],self.list[k+1] = self.list[k+1],self.list[k]
            k += 1
        return self.list[-1]


check = MRUQueue(8)
# check.fetch(3)
print(check.fetch(3))
print(check.fetch(5))
print(check.fetch(2))
print(check.fetch(8))





    
        

