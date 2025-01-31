n = int(input())
ans = 0
for i in range(n):
    check = []
    check = list(map(int,input().split()))
    if sum(check) >= 2:
        ans += 1
print(ans)
