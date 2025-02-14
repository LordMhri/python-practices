n,k = map(int,input().split())

nums = list(map(int,input().split()))

left = 0
summ = 0

ans = 0
for right in range(n):
    summ += nums[right]
    while summ > k:
        summ -= nums[left]
        left += 1
    ans += right - left + 1

print(ans)