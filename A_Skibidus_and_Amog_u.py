n = int(input())
for _ in range(n):
    word = input()
    length = len(word)
    if length >= 2:
        ans = ""
        ans += word[:length-2] + "i"
        print(ans)
    else:
        print("")