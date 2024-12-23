def minMeetingRooms(intervals) -> int:
    start = sorted(interval[0] for interval in intervals)
    end = sorted(interval[1] for interval in intervals)
    i = 0
    j = 0
    rooms = 0
    ans = 0
    while i < len(start) and j < len(end):
        if end[j] > start[i]:
            rooms += 1
            i += 1
        else:
            j += 1
            rooms -= 1
        
        ans = max(rooms,ans)
    
    return ans

intervals = [(0,40),(5,10),(15,20)]

print(minMeetingRooms(intervals))


Output = 2
