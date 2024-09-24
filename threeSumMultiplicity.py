from collections import Counter
import math
def threeSumMultiplicity(arr:list[int],target:int) -> int:
    ans = 0
    arr.sort()
    n = len(arr)
    mod = 10 ** 9 + 7
    freq = Counter(arr)
    for i in range(n):
        curr = arr[i]
        left = i+1
        right = n - 1
        while left < right:
            if curr + arr[left] + arr[right] < target:
                left += 1
            elif curr + arr[left]+ arr[right] > target:
                right -= 1
            else:
                if arr[left] != arr[right]:
                    ans += freq[curr] * freq[arr[left]] * freq[arr[right]]
                elif curr == arr[left]:
                    ans += math.comb(freq[curr],2) * freq[right]
                elif curr == arr[right]:
                    ans += math.comb(freq[curr],2) * freq[left]
                elif arr[right] == arr[right]:
                    ans += math.comb(freq[right] , 2) * freq[curr]
                elif curr == arr[left] == arr[right]:
                   ans += math.comb(freq[curr], 3)
                   break
                left += 1
                right -= 1
                    
    print(freq)
    return ans % mod

'''
doesn't exactly work but on the right track

'''


arr = [1,1,2,2,3,3,4,4,5,5]
target = 8

print(threeSumMultiplicity(arr,target))