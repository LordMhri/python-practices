def validPalindrome(s:str) -> bool:
    st = ''
    #remove non alphanumeric characters
    for i in range(len(s)):
        if s[i].isalnum():
            st += s[i].lower()
    
    #check if the resulting value is a palindrome
    left = 0
    right = len(st) - 1
    while left <= right:
        if st[left] != st[right]:
            return False
        left += 1
        right -= 1
    return True

#can be done in constant space and linear time complexity


s = "race a car"
print(validPalindrome(s))
    
    
'''
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

