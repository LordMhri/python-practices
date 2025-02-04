n = int(input())
for i in range(n):
    t1,t2 = map(str,input().split())
    lt1 = len(t1) - 1
    lt2 = len(t2) - 1
    if t1[lt1] == 'S' and t1[lt1] == t2[lt2]:
        if lt1 > lt2:
            print("<")
        elif lt2 > lt1:
            print(">")
        else:
            print("=")
    elif t1[lt1] == 'L' and t1[lt1] == t2[lt2]:
        if lt1 < lt2:
            print("<")
        elif lt2 < lt1:
            print(">")
        else:
            print("=")
    elif t1[lt1] == 'L':
        print(">")
    elif t2[lt2] == 'L':
        print("<")
    elif t1[lt1] == 'S':
        print("<")
    elif t2[lt2] == 'S':
        print(">")
    else:
        print("=")