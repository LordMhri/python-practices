n,m = map(int,input().split())


nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
ans = [0] * (n + m)
i = 0
j = 0

k = 0

while i < n and j < m:
    if nums1[i] < nums2[j]:
        ans[k] = nums1[i]
        i += 1
    else:
        ans[k] = nums2[j]
        j += 1
    k += 1

while i < n:
    ans[k] = nums1[i]
    i += 1
    k += 1
while j < m:
    ans[k] = nums2[j]
    j += 1
    k += 1

print(*ans)