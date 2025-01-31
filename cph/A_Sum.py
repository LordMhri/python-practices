n = int(input())

for i in range(n):
    lst = list(map(int,input().split()))
    lst = sorted(lst)
    if sum(lst[:2]) == lst[2]:
        print("YES")
    else:
        print("NO")