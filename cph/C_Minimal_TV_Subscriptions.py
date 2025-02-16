from collections import Counter
t = int(input())

for _ in range(t):

    n,k,d = map(int,input().split())

    arr = list(map(int,input().split()))

    count = Counter(arr[:d])

    left = 0

    minimum = len(count)

    # minimum = min(len(count),minimum)
    for right in range(d,n):
        count[arr[left]] -= 1
        if count[arr[left]] == 0:
            del count[arr[left]]
        left += 1
        
        count[arr[right]] += 1
        minimum = min(len(count),minimum)

        


    print(minimum)




'''
it is a sliding window problem with window size d
which is the number of days

there are k unique elements in the array

the array size is n

so for any given array my window size will be d
and im supposed to find the minimum number of unique elements in that windo
as i slide it






'''