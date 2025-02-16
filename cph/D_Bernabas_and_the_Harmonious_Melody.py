from collections import Counter

def is_palindrome(s):
    return s == s[::-1]


t = int(input())
for _ in range(t):
    n = int(input())
    string = input()

    freq = Counter(string)
    #needed to store the frequency to not move 
    #where the character doesnt exist

    

    for i in range(len(n)):
        count = 0
        left = i
        right = n-1
        while left < right:





'''

for abcaacab
the thought process is to pick a candidate which is the element we're iterating on 
so 'a' for the first iteration and then 

for 'a' remove 'a' itself and check if we can find a palindrome
if yes then we should save that count and continue on to the next character which is b
if not we check if we were to remove the 'a' from the back
if we can find a palindrome
if yes then  update the count stop there and go on to the next character 
if not then continue removing that character as long as the count of that character is less 
than the count of the character in the map


now when checking if it is a palindrome or not 
creating a new string will increase the complexity and make this unfeasible

so either we should find a new way of checking if it is a palindrome or not or maybe find a 
better clever way to do things


also we do this for elements of the string



'''
