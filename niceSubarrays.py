from collections import Counter
'''


Given an array of integers nums and an integer k. 
A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

'''


def numberOfSubarrays(nums: list[int], k: int) -> int:
    '''
    I see a sliding window to check if our current window/subarry exceeds k or not
    and a dictionary to keep track of the odd numbers in the subarray


    nums = [1,1,2,1,1], k = 3

    odd = 0:yes,1:yes,2:no,3:yes,4:yes

    indices = [0,1,3,4]

    increase window till we get to k
    then when we reach k check the number of odd elements inside the window
    if they're equal to k then we have a nice subarray in our hands so increment ans by 1

    i = 0,dictionary = {1:1},windowsize = 1
    i = 1,dictionary = {1:2},windowsize = 2
    i = 2,dictionary = {1:2,2:1},windowsize = 3
    WINDOWSIZE equal to k but number of odd numbers insdide the window are not equal to k
    so continue increasing window size
    i=3, dictionary = {1:3,2:1}, windowSize = 4
    windowSize is greater than k and the number of odd numbers inside the window are equal to k
    so decrease the window size and while doing so remove the left most element from the dictionary
    so we must have a left pointer
    i = 4,dictionaty = {1:2,2:1},window size = 3 but the subarray we have now isnt a nice one so keep expanding to the rigth
    i = 5,dictionary = {1:3,2:1},windos size = 4,we have a nice subarray so incease ans by 1

    we've reached the end so return ans  = 2



    a better approach is to keep track of the number of odd numbers in an array and when i reach the needed count
    increase ans and then move the left pointer a bit to the right and if the left pointer is not divisible by 2 
    decrease oddcount by 1   

    nums = [1,1,2,1,1], k = 3
    ans = 0
    oddCount = 0
    left = 0
    for right in range(len(nums)):
        if nums[right] % 2 == 1 increase oddCount by 1
        if current window is equal to or exceeds k:
            check if oddCount is also equal to or exceeds k
    '''
    oddCount = 0
    ans = 0
    prefix_count = Counter({0:1})
    for num in nums:
        if num % 2 == 1:
            oddCount += 1
        
        if oddCount - k in prefix_count:
            ans += prefix_count[oddCount-k]
        
        prefix_count[oddCount] += 1

    return ans

nums = [1,2,1,3,6,1]
k = 3

print(numberOfSubarrays(nums,k))