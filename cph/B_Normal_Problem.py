t = int(input())  
for _ in range(t):
    a = input()
    mapp = {'q':'p','p':'q','w':'w'}
    ans = ''.join(mapp[c] for c in reversed(a))  
    print(ans)