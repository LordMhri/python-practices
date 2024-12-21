def intervalIntersection(self, firstlist: list[list[int]], secondlist: list[list[int]]) -> list[list[int]]:
    sl1 = len(firstlist)
    sl2 = len(secondlist)

    ans = []
    i = 0
    j = 0
    while i < sl1 and j < sl2:
        start1,end1 = firstlist[i]
        start2,end2 = secondlist[j]

        start = max(start1,start2)
        end = min(end1,end2)

    
        if start <= end:
            ans.append([start,end])

        if end1 < end2:
            i += 1
        else:
            j += 1
        
    return ans if not ans else []