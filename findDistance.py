def findTheDistanceValue(arr1: list[int], arr2: list[int], d: int) -> int:
    ans = 0
    arr2.sort()
    for i in range(len(arr1)):
        good = True
        left = 0
        right = len(arr2) - 1
        while left <= right:
            mid = (left + right) // 2
            if abs(arr1[i] - arr2[mid]) <= d:
                good = False    
                break
            elif arr2[mid] < arr1[i]:
                left = mid + 1
            else:
                right = mid - 1
        if good:
            ans += 1

    
    return ans
arr1 = [4,-3,-7,0,-10]
arr2 = [10]
d = 69

print(findTheDistanceValue(arr1,arr2,d))