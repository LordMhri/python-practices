def sign(num):
    return num >= 0

n = int(input())
for _ in range(n):
    m = int(input())
    arr = list(map(int,input().split()))
    

    ans = 0
    i = 0

    while i < m:
        j = i
        maxx = arr[i]

        while j < m and sign(arr[j]) == sign(arr[i]):
            maxx = max(maxx,arr[j])
            j+=1
        ans += maxx
        i = j 

    print(ans)       

