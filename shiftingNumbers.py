def rangeAddition(length,updates):
    shiftArray = [0] * (length + 1)
    for i in range(len(updates)):
        left,right,direction = updates[i]
        shiftArray[left] += direction
        if right + 1 < len(shiftArray):
            shiftArray[right + 1] -= direction 

    prefix = [shiftArray[0]]
    for i in range(1,length):
        prefix.append(prefix[i-1] + shiftArray[i])
    

    return prefix

print(rangeAddition(5,([1,3,2],[2,4,3],[0,2,-2])))
