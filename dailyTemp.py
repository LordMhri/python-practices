def dailyTemperatures(temperatures: list[int]) -> list[int]:
    pair =[] #stores temp along with indices , monotonically decreasing stack
    n = len(temperatures)     
    ans = [0] * n

    for i in range(n):
        curr = temperatures[i]
        #if our stack exists and the top tempreature is less than the current one
        while pair and pair[-1][0] < curr:  
            idx = pair.pop()[1] #find where this lesser tempreature exists in the pair
            # at that index update answer array to the distance between the lesser temp 
            # and the current number we're on i.e i
            ans[idx] = i - idx 
        #if pair is empty or the current temp is smaller than the last biggest temp in pair
        #append the current temp along with the index because it is smaller
        pair.append([curr,i])
    return ans
    
            