def maxSubarray(nums:list[int])->int:
        #brute force solution
        '''
        for every number we increase our window size by 1
        then store the sum and check if it is bigger than our maxSum if so update it if not continue

        this is done for each element and for every element so this becomes
        O(n) for each element and then O(n) for every element 
        so this becoms O(n^2) and the space used would be
        O(n) if we count the answer array if not then O(1) 

        '''


        #optimized solution
        '''
        As an insight from the brute force solution we can see there are some redundant operations being done
        like summing up again and again the same values for different i values
        so if we kept a running sum then we'd avoid repeating additions

        nums = [-2,1,-3,4,-1,2,1,-5,4]
        prefixSum = [-2,-1,-4,0,-1,1,2,-3,-1]

        so one idea is to have a maxSum = nums[0]
        then whenever the prefixSum is bigger than maxSum 
        we know that there is something good going on so we should somehow save that starting point
        and it's end in a separate tuple or list or something like that then when we're finshed with this 
        loop return sum(nums[start:end])

        let's go through one example

        so start is intialized as -2 and the end is 0 or negative 1 or something like that
        so start = -2
            found something better than start end = -1 
        so that's our best position right now 
        start = 0
        end = 1
        then we go to -4 -4 is  

        ngl im cooking anyways yes then we go to -4 -4 is  a bad number
        draggin the prefix sum down so what should we do here?
        we should reset the running sum to 0 and start a new subarray from the next element



        '''
        currSum = 0
        maxSum = nums[0]
        for i in range(len(nums)):
            if currSum < 0:
                currSum = 0
            currSum += nums[i]
            maxSum = max(currSum,maxSum)
        
        return maxSum

print(maxSubarray([-2,1,-3,4,-1,2,1,-5,4]))
       
        