
n = int(input())
word = input()
ans = ""
i = 0
summ =0
while summ < n:
    i += 1
    summ += i
    ans += word[summ-1]
print(ans)

'''
6
baabbb

b 1
aa 2
bbb 3

3-2 = 1

'''