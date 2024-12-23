from collections import Counter
def divisibleSubstrings(s):
    alphabets = ["ab","cde","fgh","ijk","lmn","opq","rst","uvw","xyz"]
    mapping = Counter()
    i = 1
    for alpha in alphabets:
        mapping[alpha] = i
        i += 1
    ans = 0
    n = len(s)

    #O(n^2) solution but will do for now
    #I think using another dictionary and the method for the sum divisible by k question
    #this can potentially be further reduced to an O(n) solution
    for i in range(n):
        _sum = 0
        for j in range(i,n):
            _sum += mapping[s[i]]
            if _sum % (j-i+1) == 0:
                ans += 1
    return ans

print(divisibleSubstrings("asd"))