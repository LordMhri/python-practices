from collections import Counter
def countCharacters(words: list[str], chars: str) -> int:
    ans = 0
    chars_dict = Counter(chars)
    for word in words:
        word_dict = Counter(word)
        flag = True
        for key,val in word_dict.items():
            if val > chars_dict[key]:
                flag = False
                break
           
        if flag == True:
            ans += len(word)
                
        
    return ans


words = ["cat","bt","hat","tree"]
chars = "atach"

print(countCharacters(words,chars))