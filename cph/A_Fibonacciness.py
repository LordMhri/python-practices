'''
6
1 1 3 5
1 3 2 1
8 10 28 100
100 1 100 1
1 100 1 100
100 100 100 100


1 1 2 3 5
1 1 

'''
n = int(input())
for _ in range(n):
    arr = list(map(int,input().split()))
    first = arr[0] + arr[1]
    second = arr[2] - arr[1]
    mode1  = arr[:2]  + [first]+ arr[2:]
    mode2  = arr[:2] +[second] +  arr[2:]
    ans = 0
    temp = 0
    for i in range(2,5):    
        if mode1[i-1] + mode1[i-2] == mode1[i]:
            temp += 1
    for i in range(2,5):
        if mode2[i-1] + mode2[i-2] == mode2[i]:
            ans += 1 
    print(max(ans , temp))


