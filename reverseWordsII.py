def reverseWords(words):
    def reverse(s,i,j):
        while i < j:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
    i = 0 #i is supposed to hold the start of the string
    j = 0 #j is supposed to hold the end of the string  
    while j < len(words):
        if words[j] == ' ':#we've found an empty string therfore we need to reverse the string right before it
            reverse(words,i,j-1)
            i = j + 1 #reverse the word and move i to the start of the next string to be reversed
        elif j == len(words) - 1:#this checks to see if we're at the end and if we are reverse the last string
            reverse(words,i,j)
        j += 1
    #now we have a jumbled array of letters
    #we reversed each of the words inside the complete sentence 
    #now we want to reverse the place of these indiviual words 
    reverse(words,0,len(words) - 1)     #so we reverse the whole thing and find our answer
    return words




word = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
new = reverseWords(word)


    







word = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]

ans = ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
print(reverseWords(word))