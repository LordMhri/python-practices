from math import ceil

k, start, end = map(int, input().split())

count = 0

if k == 1:
    count = end - start + 1
else:
    if start % k == 0:
        first_divisible = start
    else:
        first_divisible = start + (k - start % k)
    
    if end % k == 0:
        last_divisible = end
    else:
        last_divisible = end - (end % k)
    
    if first_divisible > end or last_divisible < start:
        count = 0
    else:
        count = (last_divisible - first_divisible) // k + 1

print(count)


'''
return floor / ceil

for 2 -4 4
the answer is -4,-2,0,2,4 so 5 numbers

4--4 = 8 / 2 = 4

if the range includes zero that might mess things up

2 1 12
2 4 6 8 10 12

6 numbers

12-1 = 11 / 2 = 5.5 so floor?

1 1 10

every number in the range 1 10 inclusive
so 10 numbers


1 -2 10 1-10 and -2 -1 0 so 13

so for any number including zero we add one 

if  k == 1 then every number in the range we add the zero conition at the end

if k is something else we can return ceiling 


'''