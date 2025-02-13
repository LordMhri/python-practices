n = int(input())
coins = list(map(int,input().split()))
coins.sort(reverse=True)
left = sum(coins)
ans = 0


if n == 1:
    print(1)
    exit()

my_coins = 0
for i in range(n):
    if left < my_coins:
        break
    else:
        left -= coins[i]
        my_coins += coins[i]
        ans += 1

print(ans)
'''
3
2 1 2

after sorting 2 2 1
sum is 5 

so decrease 2 from 5 and add one to my coin count so coin count = 1,left = 3
left > 



given 2 coins
with value 2 each so 
2
2,2

left = 4
my_coins = 0
ans = 0

left - coins[0] =  2 > 0 -> my_coins
my_coins += 2 =2

left-coins[1] = 2 - 2 = 0
my_coins += 2= 4

so stop


'''