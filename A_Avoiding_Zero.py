n = int(input())

for _ in range(n):
    m = int(input())
    arr = list(map(int,input().split()))
    sum_ = sum(arr)
    if sum_ == 0:
        print("NO")  
    else:
        print("YES")
        if sum_ > 0: 
            print(*(sorted(arr,reverse=True)))
        else:
            print(*(sorted(arr)))

    

