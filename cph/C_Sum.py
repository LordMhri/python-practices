n = int(input())

for i in range(n):
    lst = list(map(int,input().split()))
    lst = sorted(lst)
    if lst[0] + lst[1] == lst[2]:
        print("YES")
    else:
        print("NO")