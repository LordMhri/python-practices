def carPooling(trips,capacity):
    event = []
    for trip in trips:
        num,pick,drop = trip
        event.append((pick,num))
        event.append((drop,-num))
    
    event.sort(key=lambda x: (x[0], x[1]))
    curr_cap =0
    for _,passengers in event:
        curr_cap += passengers
        if curr_cap > capacity:
            return False


    return True

print(carPooling([[2,1,5],[3,3,7]],4))