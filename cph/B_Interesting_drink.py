n = int(input())
price_arr = list(map(int, input().split()))
days = int(input())

todays = []
for i in range(days):
    todays.append((int(input()),i))
todays.sort()
price_arr.sort()



prefix_price = [0]
for i in range(len(price_arr)):
    prefix_price.append(prefix_price[-1] + price_arr[i])

days_ptr = 0
price_ptr = 0

ans = [0] * days

prev_ptr= 0

curr_ans = 0
    
    
for coins,idx in todays:
    while price_ptr < n and price_arr[price_ptr] <= coins:
        curr_ans += 1
        price_ptr += 1
    ans[idx] = curr_ans 

for i in range(len(ans)):
    print(ans[i])

    




'''
i can sort the price arr and for each day check which store he can buy
the beverage he wants

that would be O(n^2) since for each day im checking whether he can buy the drink or not

how do i optimize it?

what redundant operation is being done

if coin_today was sorted
1,3,10,11


if price was sorted
3,6,8,10,11

1 is less than the first price so i can stop there

i 
but the prices arent unique so i cant just stop the moment i find the same price because the next
price can also be the same as the current one

the prices can sort of be made unique by having the prefix sum of the price_arr
the array is sorted and there are no negative values so
for each value in the prefix sum i know that whatever is next to it is atleast bigger than what i have here
so for 3 10 8 6 11
and it is sorted
3 6 8 10 11

the prefix sum will be 

1,3,10,11 -> day_coins
^
0,3,9,17,27,38
  ^ 

with 1 coin i cant buy anything so
i dont add anything to my answer


so the answer for 1 coins is 0

with 3 coins i can buy a beverage so
add 1 to answer and move both ptrs? 

so the answer for 3 coins is 1

with 10 coins i can buy whatever i could have bought with 3 coins plus whatever i can buy with 
the remaining 7 coins

so the answer starts from whatever it left off which is 1
and i go until i get to a value bigger or equal to 10

so my ptr was at 3 because 3-0 is 3  
        0,3,9,17,27,38
now move my cost_ptr until i get to a value where 
the difference between the consecutive elements is equal to or greater than 10 which is 
at 27 and 17 and add curent ptr - former_ptr place
          

'''


'''

0,3,9,17,27,38


'''