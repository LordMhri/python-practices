def merge(nums1:list[int],nums2:list[int]) -> list[int]:
    ans = [0] * (len(nums1) + len(nums2))
    n1 = len(nums1)
    n2 = len(nums2)

    i = 0
    j = 0

    k = 0
    while i < n1 and j < n2:
        if nums1[i] < nums2[j]:
            ans[k] = nums1[i]
            i += 1
        else:
            ans[k] = nums2[j]
            j += 1
        k += 1
    
    while i < n1:
        ans[k] = nums1[i]
        i += 1
        k += 1
    while j < n2:
        ans[k] = nums2[j]
        j += 1
        k += 1

    return ans

def mergeSort(nums:list[int])-> list[int]:
    if len(nums) == 1:
        return nums
    len1 = len(nums)
    nums1 = nums[0:len1//2]
    nums2 = nums[len1//2:]

    nums1 = mergeSort(nums1)
    nums2 = mergeSort(nums2)

    return merge(nums1,nums2) 
    