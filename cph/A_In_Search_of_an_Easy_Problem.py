def iimp():
  return int(input())
def limp():
  return list(map(int,input().split()))

n = iimp()
lst = limp()
if sum(lst) > 0:
  print("HARD")
else:
    print("EASY")
