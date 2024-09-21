def mergeIntervals(intervals: list[list[int]]) -> list[list[int]]: 
    if not intervals:
        return []
    
    #sort the intervals to make things easier
    intervals = sorted(intervals)
    answer = [intervals[0]] #we know for sure that at least the first element is in the interval
    
    for i in range(1, len(intervals)): #we've added the first one so no need to check
        #if the ending interval of the last element in answer like
        #answer = [[1,3]], intervals = [[1,3],[2,6]] compare 3 and 2 
        if answer[-1][1] >= intervals[i][0]: 
            #for the example if 3 is found to be bigger than 2 which it is
            #whatever is the maximum of 1 and 6 to be the end interval for the last element of
            #our answer
            answer[-1][1] = max(answer[-1][1], intervals[i][1])   
        else: #no overlapping occurs
            #just add the current one to the answer array
            answer.append(intervals[i])
    
    return answer

intervals = [[1, 4], [0, 2], [3, 5]]
print(mergeIntervals(intervals))

'''
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


'''