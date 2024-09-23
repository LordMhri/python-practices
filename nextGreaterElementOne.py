def nextGreaterElement(nums1:list[int],nums2:list[int]) -> list[int]:
    ans = []
    for i in range(len(nums1)):
        found = False
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                count = j
                while count < len(nums2):
                    if nums2[count] > nums1[i]:
                        ans.append(nums2[count])
                        found = True
                        break
                    count += 1
                if not found:
                    ans.append(-1)
                break
    
    return ans

# works but there has to be an efficient solution for this ,this is
# a O(n^2) time solution and i didn't use stack ,it is tagged as stack
# so there has to be a better solution using stack




nums1 = [4,1,2]
nums2 = [1,3,4,2]

print(nextGreaterElement(nums1,nums2))

'''
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

'''