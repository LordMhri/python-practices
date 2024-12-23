from collections import Counter
def compress(s):
    mapp = Counter()
    for i in range(len(s) - 1):
        if s[i].isalpha():
            mapp[s[i]] += int(s[i+1])
    ans = ''
    for w in sorted(mapp):
        ans += w
        ans += str(mapp[w])
    
    return ans



s = "a3c9b2c1"
print(compress(s))
        