n = int(input())

for _ in range(n):
    word = input()
    ans = 0
    flag = False
    for i in range(len(word) -1 ):
        if word[i] == word[i+1]:
            flag = True 
            break
    if flag:
        print(1)
    else:
        print(len(word))    