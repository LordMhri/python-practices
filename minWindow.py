from collections import Counter
def minWindow(self, s: str, t: str) -> str:
    left = 0
    right = 0
    ans = ""
    tmap = Counter(t)
    smap = Counter()
    while right < len(s):
        smap[s[right]] += 1
        while tmap <= smap:#as long as tmap is a subset of smap
            if not ans or right - left + 1 < len(ans): #if current window is less than length of my answer
                ans = s[left:right+1]
            
            smap[s[left]] -= 1
            if smap[s[left]] == 0:
                del smap[s[left]]
            left += 1
        right += 1
    
    return ans
