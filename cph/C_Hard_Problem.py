t = int(input()) 

for _ in range(t):
    m, a, b, c = map(int, input().split())  
    
    s1 = min(m, a) 
    s2 = min(m, b)  
    
    remaining_seats = (2 * m) - (s1 + s2)
    
    
    left = min(remaining_seats, c)
    
    
    print(s1 + s2 + left)

'''
5
10 5 5 10
3 6 1 1
15 14 12 4
1 1 1 1
420 6 9 69


10
5 in the front row
5 in the back row
so 10 seats left 
and then 10 monkeys with no preference sit there

3
6 in the front row not possible becuase 3-6 is less than 0
so only 3 monkeys in the front row
1 in the back row possible because 3-1 is greater than 0
so 1 monkey in the back
1 has no prefernce so a total of 3+1+1 monkeys can sit

15
14 in the front row possible becuase 15-14>= 0
then 12 in the back row possible because 15-12 >= 0 
then 4 monkeys can be seated where we have 2*m = 2*15 - 14 - 12 = 4
so 4 monkeys can be seated there

so the algorithm is 
for the front row check if m-a is bigger than -1 if so then m-a is front row
if not min(m,a) is the front row
for the second row check if m-b is bigger than -1 if so then m-b is second row
if not min(m.b) is the second row
for the monkeys who dont care see how many seats are left
left = 2*m - front_row - second_row
then add left + front_row + second_row to the answer


'''