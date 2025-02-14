n,k = map(int,input().split())

nums = list(map(int,input().split()))

left = 0
summ = 0

res = 0
ans = float('inf')
for right in range(n):
    summ += nums[right]
    while summ >=  k:
        res += (n-right)
        summ -= nums[left]
        left += 1
    

print(res)