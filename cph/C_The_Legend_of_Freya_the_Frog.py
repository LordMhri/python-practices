from math import ceil
n = int(input())
for i in range(n):
    x,y,moves = map(int,input().split())

    x_moves = ceil(x/moves)
    y_moves = ceil(y/moves)


    if y_moves > x_moves:
        ans = 2*y_moves 
    else:
        ans = 2*x_moves - 1
    
    print(max(2*y_moves,2*x_moves-1))