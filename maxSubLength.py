def maxSubLength(nums):
    stack = []
    maxLen = 0
    for num in nums:
        if not stack or stack[-1] >= num:  # Compare with the last element in the stack
            stack.append(num)  # Continue the semi-decreasing trend
        else:
            maxLen = max(len(stack), maxLen)  # Update max length
            stack = [num]  # Reset stack with the current number

    maxLen = max(len(stack), maxLen)  # Check the final subarray
    return maxLen


# Example Test Case:
print(maxSubLength([57, 55, 50, 60, 61, 58, 63, 59, 64, 60, 63]))
