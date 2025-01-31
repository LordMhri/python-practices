def iimp():
    return int(input())

def limp():
    return list(map(int, input().split()))

n = iimp()
proportions = limp()
summ = sum(proportions)
print(round(summ/n,12))