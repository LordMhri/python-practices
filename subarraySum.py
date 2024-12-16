from collections import Counter

nums = [1,1,1]
k = 2


#brute force solution
'''
for every number check if we could add another arr value and get k
so [2,3] 2 + 3 = 5 so ans = 1
and then do this until we reach the end and repeat for every value

'''

def bruteForce(nums:list[int],k:int)->int:
    ans = 0
    for i in range(len(nums)):
        
        summ = nums[i]
        print(f"Summ is {summ} at index i = {i}")
        for j in range(i+1,len(nums)):
            print(f"Summ is {summ} at index i = {i} and j = {j}")
            if summ == k:
                ans += 1
            summ += nums[j]
    
    return ans


print(bruteForce(nums,k))

''''
Logic behind the implementation is
summ of nums[j:i] = k

so summ(nums[j]) meaning summ of the arrays leading upto j 
and summ(nums[i-1]) meaning sum of the arrays leading up to i 

we want to check if the difference between them is equal to k
the way to efficiently find the sums are to use a prefix sum

so essentially we're asking if
prefix[j] - prefix[i-1] == k
which also means 
prefix[j] - k = prefix[i-1]

so the plan is to check if we've encountered such an example
and the efficient way would be to save the prefix and then check in the dictioanry
if prefix-k exists

we store the prefix so that if in the future
when we're checking if our inital check 
which was prefix[j] - k exists in the dictionary and it does then
that means we've found a correct one

meaning lets say we have 5 as a prefix 
so we store {5:1} 

then when we check if prefix - k in mapp
and our prefix - k equals 5

so at some eariler point we had a prefix sum equaling 5
let's call this prefix[i-1] = 5
and no we have prefix - k = 5
so we've seen it before and we add how many times we've seen it to our answer
and finish


Time O(n)
Space O(n) -> for storing the map,prefix and ans



'''

def subarraySum(nums: list[int], k: int) -> int:
    mapp = Counter({0:1})
    ans = 0  
    prefix = 0
    for num in nums:
        prefix += num
        if prefix - k in mapp:        
            ans += mapp[prefix -k]

        mapp[prefix] += 1

    return ans

subarraySum(nums = [2,3,6,5,4,1,1],k=5)