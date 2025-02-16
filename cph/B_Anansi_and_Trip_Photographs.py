t = int(input())
for _ in range(t):
    row,min_diff = map(int,input().split())

    arr =  list(map(int,input().split()))

    arr.sort(reverse=True)

    back_row = arr[:row]
    front_row = arr[row:]

    # print(back_row)
    # print(front_row)

    for j in range(row):
        if back_row[j] < front_row[j] + min_diff:
            print("NO")
            break
    else:
        print("YES")