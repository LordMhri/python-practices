

def insertionSort(nums: list[int]) -> list[int]:
    # looks like a two pointer algorithm
    # assume the first element is already sorted, that's why 
    # we start from 1
    # lets go through the algo with an example
    # [4,1,2,4,5]
    # key = nums[i] = nums[1] -> = 1
    #  j = i- 1 -> j = 0
    # while j>=0 is true 
    # and key < nums[j] is also true since key = 1 and nums[j] = nums[i-1] = 4
    # 1 < 4 if so
    # then nums[j+1] = nums[j] -> nums[i-1+1]  -> nums[i] -> nums[1] = nums[0]
    # nums[1] was 1 and nums[0] was 4
    # now nums[0] will be 1, j -= 1 -> j = -1 
    # which is less than 0 so we step out of the while loop
    # and nums[j+1] which is nums[0] will be set to key (1)
    # resulting array: [1, 4, 2, 4, 5]
    for i in range(1,len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j] #shift elements to the right
            j -= 1
        nums[j+1] = key #insert key at correct pos



