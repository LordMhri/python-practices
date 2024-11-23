def sumMinimumSubArray(arr:list[int]) -> int:
    #find the left span of each element
    n = len(arr)
    left = [0] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        left[i] = i - stack[-1] if stack else i+1
        stack.append(i)



    # find the right span of each element
    stack = []
    right = [0] * n
    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        right[i] = stack[-1] - i if stack else n-i
        stack.append(i)

    #compute prefix sum
    ans = 0
    mod = 10**9 + 7
    for i in range(n):
        ans += arr[i] * left[i] *right[i]
        ans%= mod
    
    return ans

print(sumMinimumSubArray([3,1,2,4]))