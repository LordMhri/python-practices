def rangeSum(nums: list[int], left: int, right: int) -> int:
    new = []
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            new.append(current_sum)
    
    new.sort()
    print(f"new is {new}")
    pre = [new[0]]
    for i in range(1,len(new)):
        pre.append(pre[i-1] + new[i])
    
    return pre[right-1] - (pre[left-2] if left > 1 else 0)

nums = [1,2,3,4]
n = 4
left = 1
right = 5
print(rangeSum(nums,1,5))