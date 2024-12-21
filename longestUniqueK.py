from collections import Counter

def longestUniqueKey(s:str,k:int) -> int:
    max_len = 0
    mapp = Counter()
    left = 0
    right = 0
    while right < len(s):
        mapp[s[right]] += 1

        while len(mapp) > k:
            mapp[s[left]] -= 1
            if mapp[s[left]] == 0:
                del mapp[s[left]]
            left += 1
        
        max_len = max(max_len, right - left + 1)
        right += 1
 

    return max_len

print(longestUniqueKey("eceba",k=2))

