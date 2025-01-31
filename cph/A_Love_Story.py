n = int(input())
string = "codeforces"
for i in range(n):
    ans = 0
    new_string = input()
    for i in range(10):
        if new_string[i] != string[i]:
            ans += 1
    print(ans)