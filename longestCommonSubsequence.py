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

''
'''
4 1 7 3 19 12


1 4 7 3 19 12

1 3 7 



1 7 4 3 19 12
1 7 3 4 19 12

1 7 3 19 4 12
1 4 7 










1 3 7 4
1 4 7 3

3


4 1 7

1 4 7

11
 
1 7 4

1 4 7 




8 7 4 9 3 12 9 1 4



'''