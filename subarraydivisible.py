from collections import Counter
def subarraysDivByK(nums: list[int], k: int) -> int:
    check = Counter({0:1})
    ans = 0
    prefix = 0
    for num in nums:
        prefix += num
        mod = prefix%k
        if mod < 0:
            mod += k
            

        if mod in check:
            ans += check[mod]

        check[mod] += 1

    return ans       

nums = [4,5,0,-2,-3,1]
k = 5

print(subarraysDivByK(nums,k))