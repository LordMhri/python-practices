def nextPermutation(nums:list[int]):
    n = len(nums)
    if n  <= 1: #get easy base cases out the way
        return
    
    num = None 
    for i in range(n- 2,-1,-1):
        if nums[i] < nums[i + 1]: 
            num = i # the index of the number to be swapped
            break
    if num is None:
        nums.reverse()
        return
    
    for i in range(n- 1,num,-1):
        if nums[i] > nums[num]:  # swapping here
            nums[i] , nums[num] = nums[num], nums[i]
            break 
    
    nums[num+1:] = reversed(nums[num+1:]) #reverse the remaining items
    

    
    
    
nums = [1,2,3]

nextPermutation(nums)

print(nums)
'''
Input: nums = [1,2,3]
Output: [1,3,2]


[1,2,3,2,1]
Expected
[1,3,1,2,2] starting from the right find the first number that 
is bigger than the one to the left of it
the number on the left of it is the number we have to swap with 
for [1,2,3,2,1] 3 is the first number which is bigger than the one next to it i.e 2
so swap 2 and 3 -> [1,3] then the remaining part of the array [2,2,1] reverse it then done

if there is no number bigger than the one next to it like [5,4,2,1] then reverse and answer 

'''
    