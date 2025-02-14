n,k = map(int,input().split())

nums = list(map(int,input().split()))

left = 0
summ = 0

ans = float('inf')
for right in range(n):
    summ += nums[right]
    while summ >= k:
        ans = min(ans,right-left+1)
        summ -= nums[left]
        left += 1

ans = ans if ans != float('inf') else -1
print(ans)

