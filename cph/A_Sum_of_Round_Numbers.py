def iimp():
  return int(input())

def limp():
  return list(map(int, input().split()))

n = iimp()
for i in range(n):
    ans = []
    num = int(input())
    summand = 1

    while num > 0: 
        if num % 10:  
            ans.append(num % 10 * 10**(summand-1))
        summand += 1
        num //= 10

    print(len(ans))
    print(*reversed(ans)) 

