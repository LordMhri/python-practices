from collections import Counter
def longestCommonSubsequence(nums):
    ans = []
    n = len(nums)
    check = Counter()
    for num in nums:
        for i in num:
            check[i] += 1
            if check[i] == n:
                ans.append(i)
    
    return ans

print(longestCommonSubsequence([[2,3,6,8],
                 [1,2,3,5,6,7,10],
                 [2,3,4,6,9]]))