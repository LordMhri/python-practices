n = int(input())


correct_sum = int(n*(n+1)/2)
current_sum = sum(list(map(int,input().split())))

print(correct_sum - current_sum)