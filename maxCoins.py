def maximumcoins(hero,monsters,coins):
    h = len(hero)
    m  = len(monsters)
    c = len(coins)
    ans = []
    #this is an O(m*n) solution and can be further optimized
    # for i in range(h):
    #     curr = 0
    #     for j in range(m):
    #         if hero[i] >= monsters[j]:
    #             curr += coins[j]
    #     ans.append(curr)


    #sort monsters and keep the association with the coins intact
    combined = list(zip(monsters,coins))

    combined.sort(key=lambda x:x[0])

    monsters,coins = zip(*combined)

    print(monsters)
    print(coins)


    return ans




heroes = [4,4]
monsters = [5,7,9,8]
coins = [1,10,9,1]

print(maximumcoins(heroes,monsters,coins))


'''
#brute force
for each hero check if we can defeat the monster if so
add  the corresponding coins to a temporrary array 

when we finish the loop for the hero append the temporrary array 
to the answer array

#there should be away to not check if my hero can defeat the
#same monsters every time
#assuming my hero array is sorted
#if hero can defeat first three monsters and herob > heroa
#i dont have to check if my hero can defeat the first three monsters also
it is a given

so i can start from where i stopped before meaning if i stopped 
before monsterc i can start from monsterd

and the current answer for the current hero would be the 
score for the previous hero

heroes = [1,4,2]
monsters = [1,1,5,2,3]
coins = [2,3,4,5,6]

for this to work monsters need to be sorted
and coins must also be sorted the same way monsters is sorted
meaning monsters after it is sorted 
looks like [1,1,2,3,5]
coins if sorted without any consideration looks like the same way
it looks right now but it should correspond to the monsters array
so it coins should be [2,3,5,4,6]
but heroes must always be sorted if we were to do this in a more efficient way


'''

