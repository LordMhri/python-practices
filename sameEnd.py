from collections import Counter
def numSameEnd(s,intervals):
    prefix = sameEnd(s)
    answer = []
    for start,end in intervals:
        start -= 1
        end -= 1
        if start == 0:
            answer.append(prefix[end])
        else:
            answer.append(prefix[end] - prefix[start - 1])
    return answer
    

def sameEnd(s):
    freq = Counter()
    ans = []
    _sum = 0
    for i in range(len(s)):
        freq[s[i]] += 1
        _sum += freq[s[i]]
        ans.append(_sum)

    return ans
print(numSameEnd("abcaab",([0,0],[1,4],[2,5])))
