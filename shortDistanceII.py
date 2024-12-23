def shortDistance(words,word1,word2):
    word1idx = -1
    word2idx = -1
    dist = float("inf")
    n = len(words)

    for i in range(n):
        if word1 == word2:
            if words[i] == word1:
                if word1idx != -1:  # If we've seen the word before
                    dist = min(dist, abs(i - word1idx))
                word1idx = i 
        else:
            if words[i] == word1:
                word1idx = i
                if word2idx != -1:#we've found the second word before
                    dist = min(abs(word2idx - word1idx),dist)
            elif words[i] == word2:
                word2idx = i
                if word1idx != -1:
                    dist = min(abs(word2idx-word1idx),dist)

    return dist
            


word1 = "makes"
word2 = "coding"
words = ["practice", "makes", "perfect", "coding", "makes"]

print(shortDistance(words,word1,word2))

'''
using a set how would this work

when i find the first occurence of the word
add it to the set

and update the first index this is for the first occurence but now
if we find the word again meaning it is in the list what we do is
update our second index and continue

    this is only for the case where the two words are the same
    if word not in set:
        update firstindex
    but if word in set:
        update the secondindex
        and also the distance


'''