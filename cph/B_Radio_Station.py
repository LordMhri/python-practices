def iimp():
  return int(input())
def limp():
  return list(map(int,input().split()))

mapp = {}
n,m = map(int,input().split())
for i in range(n):
    name,ip = map(str,input().split())
    mapp[ip] = name

for i in range(m):
   name,ip = map(str,input().split())
   print(f"{name} {ip} #{mapp[ip.rstrip(';')]}")


