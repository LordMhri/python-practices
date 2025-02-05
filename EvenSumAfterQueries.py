def sumEvenAfterQueries(nums: list[int], queries: list[list[int]]) -> list[int]:
    initial_sum = sum(num for num in nums if num%2 == 0)
    ans = []
    for query in queries:
        initial_val = nums[query[1]]
        nums[query[1]] += query[0]
        if initial_val % 2 == 1:#was odd first
            if nums[query[1]] % 2 == 0: #is even now
                initial_sum += nums[query[1]]
                ans.append(initial_sum)
            else:
                ans.append(initial_sum)
        else: #was even
            if nums[query[1]] % 2 == 1:#is odd now
                initial_sum -= initial_val
                ans.append(initial_sum)
            else: #is still even
                initial_sum += nums[query[1]] - initial_val
                ans.append(initial_sum)
               
    
    return ans

nums = [3,2]
queries = [[4,0],[3,0]]

print(sumEvenAfterQueries(nums,queries))
