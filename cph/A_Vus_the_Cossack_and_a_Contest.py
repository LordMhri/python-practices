def iimp():
  return int(input())
def limp():
  return list(map(int,input().split()))

n,m,k = map(int,input().split())
check = min(m,k)
if check >=n:
  print("Yes")
else:
  print("No")