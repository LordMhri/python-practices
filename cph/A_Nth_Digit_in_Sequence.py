n = int(input())

check = [i+1 for i  in range(n)]
check = "".join(str(i) for i in check)

ans = check[n-1]
print(ans)
    
