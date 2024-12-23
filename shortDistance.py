def shortDistance(word1,word2,words):
    word1idx = -1
    word2idx = -1
    dist1  = float("inf")
    n = len(words)
    for i in range(n):
        if words[i] == word1:
            word1idx = i
            if word2idx != -1:#we've found the second word before
                dist1 = min(abs(word2idx - word1idx),dist1)
        elif words[i] == word2:
            word2idx = i
            if word1idx != -1:
                dist1 = min(abs(word2idx-word1idx),dist1)

            
    return dist1

wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"


print(shortDistance(word1,word2,wordsDict))