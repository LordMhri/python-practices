n = int(input())

nums = list(map(int,input().split()))

first,last = -1, -1
def small_reverse(arr,i,j):
    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1
    return arr

for i in range(len(nums) - 1):
    if nums[i] > nums[i+1]:
        if first == -1:
            first = i
        last = i + 1

nums  = small_reverse(nums,first,last)

if first == -1:
    print("yes")
    print(f"1 1")
    exit()


if nums != sorted(nums):
    print("no")
else:
    print("yes")
    print(f"{first + 1} {last + 1}")



