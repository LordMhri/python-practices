def twoSum(nums:list[int],target:int)-> list[int]:
    check = {}
    for i in range(len(nums)):
        comp = target-nums[i]
        if comp in check:
            return [nums.index(comp),i]
        else:
            check[nums[i]] = comp
            
