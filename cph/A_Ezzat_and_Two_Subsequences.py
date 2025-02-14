'''
Ezzat has an array of n
 integers (maybe negative). He wants to split it into 
 two non-empty subsequences a
 and b
, such that every element from the array belongs to
 exactly one subsequence, and the value of f(a)+f(b)
 is the maximum possible value, where f(x)
 is the average of the subsequence x
.

A sequence x
 is a subsequence of a sequence y
 if x
 can be obtained from y
 by deletion of several (possibly, zero or all) elements.

The average of a subsequence is the sum of the numbers of t
his subsequence divided by the size of the subsequence.


what is the optimal startegy here?


3
3 1 2


we can choose any subsequence 
3 1 2

so 3 1 is valid and the answer is  4/2 + 2 = 4
3 + 2 is valid and the answer is 5/2 + 1 = 3.5
1 + 2 is valid and the answer is 1.5 + 3 = 4.5

it seems the most optimal way is to have the largest number divided by the least amount of numbers
duh

so how big should the divisors be? so that we can have the most optimal answer


3
-7 -6 -6

the biggest number should be divided the least amount of times
so -7 + -6 = 13/2 = -6.5 and -6 would be -12.5
-12/2 and -7 would give -13

4
17 3 5 -3

let the biggest number be by itself
so 17 alone and 3+5-3/3 = 5/3 = 1.66
17+1.66 is the best answer

'''

n = int(input())
for _ in range(n):
    m = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    # print(arr)
    ans = arr[0] + sum(arr[1:m+1])/ (m-1)
    print(ans)