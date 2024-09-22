from collections import defaultdict
def longestConsecutive(nums: list[int]) -> int:
    #needs to run in O(n) time otherwise sort and count would have sufficed
    freq = defaultdict(int)
    for num in nums: 
        freq[num] += 1
    
    '''
        {
            100: 1,
            4 : 1,
            200 : 1,
            3 : 1,
            2: 1
        } for every element check if the number before it exists like 
        for 100 check if  99 exists if 99 exists then just continue 
        because we haven't yet found the starting point for that number
        but for this number 100 99 doesn't exist so 100 must be a starting point so
        with a while loop or some sort of loop look for it's next values like 101, 102
        in our map along with their values
        
        for 4 check if 3 exists it does so ignore 4 go to 200 check if 199 exists no it doesn't so 
        200 could potentially be a starting point start a while loop and look for 201 it doesn't exist so
        go to 3 check if 2 exists it does so ignore go to 2 check if 1 exists it doesn't so 2
        could potentially be a starting point start a while loop and check for 2 + 1 it exists so increment
        a consecutive counter now at 3 check if 4 exists it does so increment counter our answer is 3 when
        we start counting we start from 1
    '''
    ans = 0
    for key,val in freq.items():
        counter = 1
        if key - 1 not in freq:#key is a starting point
            num = key
            while num+1 in freq: #while the consectutive elements exists
                counter += 1
                num +=1
            ans = max(counter,ans)
    return ans
     
nums = [0,0]
print(longestConsecutive(nums))   
    
    


'''Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''