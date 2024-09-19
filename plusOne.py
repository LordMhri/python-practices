def plusOne(digits:list[int]) -> list[int]:
    num = ''
    for n in digits:
        num+= str(n)
        
    num = int(num) + 1
    ans = []
    while num > 0:
        ans.append(num%10)
        num = num // 10
        
    return ans[::-1]