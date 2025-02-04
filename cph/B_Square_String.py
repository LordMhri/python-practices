n = int(input())

for i in range(n):
    word = input()
    length  = len(word) // 2
    if len(word) % 2 != 0:
        print("NO")
    else:
        if word[:length] == word[length:]:
            print("YES")
        else:
            print("NO")