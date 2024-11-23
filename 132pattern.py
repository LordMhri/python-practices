def find132pattern(nums: list[int]) -> bool:
    if len(nums) < 3:
        return False
    
    stack = []
    second = float('-inf')
    
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < second:
            return True
        while stack and nums[i] > stack[-1]:
            second = stack.pop()
        stack.append(nums[i])
    
    return False

print(find132pattern([-1, 3, 2, 0]))


