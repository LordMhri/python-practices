def isSubsequence(s: str, t: str) -> bool:
    k = 0

    ans = 0
    if len(s) <= 0:
        return True
    for i in range(len(t)):
        if k < len(s) and s[k] == t[i]: # if a similar char is found
            k += 1
            ans += 1
    return True if ans == len(s) else False


s = "axc"
t = "ahbgdc"

print(isSubsequence(s,t))
