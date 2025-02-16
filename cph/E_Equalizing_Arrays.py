len1 = int(input())
arr1  = list(map(int,input().split()))
len2 = int(input())
arr2  = list(map(int,input().split()))

def remove_zeroes(arr):
    new_arr = []
    for num in arr:
        if num != 0:
            new_arr.append(num)
    
    return new_arr

if sum(arr1) != sum(arr2):
    print(-1)
    exit()


i = 0
j = 0
while i < len1 and j < len2:
    if arr1[i] == arr2[j]:
        i += 1
        j += 1
    elif arr1[i] < arr2[j]:
        second_i = i
        while second_i+1 < len(arr1) and arr1[i] < arr2[j]:
            arr1[i] += arr1[second_i+1]
            arr1[second_i+1] = 0
            second_i += 1
    else:
        second_j = j
        while second_j+1 < len(arr2) and arr1[i] > arr2[j]:
            arr2[j] += arr2[second_j+1]
            arr2[second_j+1] = 0
            second_j += 1

arr1 = remove_zeroes(arr1)
arr2 = remove_zeroes(arr2)

if len(arr1) != len(arr2):
    print(-1)
    exit()
else:
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            print(-1)
            exit()
    else:
        print(len(arr1))
        exit()

'''
the process for this was a two pointer on separate arrays

5
11 2 3 5 7
4
11 7 3 7


so check if 

the first two numbers are equal 
11 and 11 they're equal so move both ptrs to the next 
at 2 and 7 2 is smaller so we need to increase 2 until it is equal to bigger than 7
so add it's next element which is 
3 so 2+3 = 5 < 7 so move on to the next element
5, 5 + 5 == 10
which is bigger than 7 

i think we can do something like this
5
11 2 3 5 7
11 5 0 5 7
11 10 0 0 7
4
11 7 3 7
11 10 0 7

so finally we would have 
11 10 0 0 7
11 10 0 7

we can remove all zeroes from the list

so 
11 10 7
11 10 7


another observation if thier sums are equal then yes a valid rearrangment of the values
in such a way that we can fulfill the requirements is possible

but when their sum aren't equal then we can rearrange t
hem in the manner that we want no matter what we do



'''

# check = []

# ls = [0,0,1,1,0,3]
# for i in range(len(ls)):
#     if ls[i] == 0:
#         continue
#     else:
#         check.append(ls[i])
    

# print(check)