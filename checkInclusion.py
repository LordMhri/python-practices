from collections import Counter

def checkInclusion(s1: str, s2: str) -> bool:
    freq = Counter(s1)
    freq2 = Counter()
    left = 0
    for right in range(len(s2)):
        freq2[s2[right]] += 1
        #window of size right - left + 1
        if right - left + 1 > len(s1): 
            freq2[s2[left]] -= 1

            if freq2[s2[left]] == 0:
                del freq2[s2[left]]
            left += 1
        
        if freq2 == freq:
            return True
    
    return False

s1 = "ab"
s2 = "eidbaooo"
checkInclusion(s1,s2)