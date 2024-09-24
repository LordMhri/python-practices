def rescueBoats(people:list[int],limit:int) -> int:
    ans = 0
    people.sort()
    left = 0
    right = len(people) - 1
    while left <= right:
        if people[left] + people[right] > limit:
            right -= 1
            ans += 1
        else:
            left += 1
            right -= 1
            ans += 1
    
    return ans

people = [3,2,2,1]
limit = 3
print(rescueBoats(people,limit))