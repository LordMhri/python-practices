def findWords( words: list[str]) -> list[str]:
    s1 = set("qwertyuiop")
    s2 = set("asdfghjkl")

    s3 = set("zxcvbnm")
    ans = []
    for word in words:
        print(set(word.lower()))
        print(s2)
        if set(word.lower()).issubset(s1) or set(word.lower()).issubset(s2) or  set(word.lower()).issubset(s3):
            
            ans.append(word)
    
    return ans

print(findWords(["hello","alaska"]))