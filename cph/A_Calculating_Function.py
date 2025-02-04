def iimp():
  return int(input())
def limp():
  return list(map(int,input().split()))

n = iimp()
if n % 2 == 0:
  print(n//2)
else:
  print(-((n+1)//2))
