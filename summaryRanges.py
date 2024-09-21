
def summaryRanges(nums: list[int]) -> list[str]:
    if not nums:
        return []
    
    ans = []
    s = ""
    ranges = []
    
    for i in range(1, len(nums)):
        if len(s) == 0: #if the string is empty add the previous number
            s += f'{nums[i-1]}'
        ranges.append(nums[i-1]) # add number to our range because they're consecutive
        if nums[i] - nums[i-1] != 1: # if the numbers aren't consecutive
            if len(ranges) != 1: #check if ranges is not just one element
                s += f"->{nums[i-1]}" # add the right range for the answer
            ans.append(s) # append s to our answer
            s = '' # restart our s
            ranges = [] # restart our ranges
    
    #this is for our last element
    if len(s) == 0: # if s is empty it means there was no previous element
        s += f'{nums[-1]}' # so just add the last element
    ranges.append(nums[-1]) #add last elem to range
    if len(ranges) != 1: # if range was not just a single element it means it had a previous one
        s += f"->{nums[-1]}" # so add the last as an extension of the previous one
    ans.append(s) #append to answer
    
    return ans


  
nums = [0,1,2,4,5,7]  
print(summaryRanges(nums))    


'''
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
'''