from collections import Counter

n = int(input())
for i in range(n):
    a  = input()
    b  = input()
    a_pointer = 0
    b_pointer = 0
    b_len = len(b)
    c  = input()
    a_len = len(a) 
    cmap = Counter(c)
    flag = True
    while b_pointer < b_len:
        char = b[b_pointer]
        if a_pointer < a_len and a[a_pointer] == char:
            a_pointer += 1
        else:
            if char not in cmap:
                flag = False
                break
            else:
                cmap[char] -= 1
                if cmap[char] == 0:
                    del cmap[char]
        b_pointer += 1
        
    
    if not flag:
        print("NO")
        break
    if a_pointer == a_len:
        print("YES")
    else:
        print("NO")

            
    '''
    a
    aaaa
    bbcc




    
    a = a so move on to the next character
    compare b and c not equal check if c exists in cmap
    yes so decrease count of c and remove if count of 'c' in c is zero
    go to the next char x
    check if x is the same as char in b
    it isnt so check if c contains x it does decremnt count then remove x
    we've moved to b so check if b is the same as b it is so move on to the next




    bx
    z
    '''

    # if a_map != bmap:
    #     print("NO")
    # else:
    #     print("YES")

    
    '''
    ab = a
    acxb = b
    cax = c

    compare a with b
    ab
    acxb
    cax

    for the length of  b:
        check if character in a == charcter in b
            if so then no problem
            we can just move on to the next
        else:
            check if char not found in a is found in c
            if it is then decrement the count of the character in c then move on to the next
            if char in a is not found in c then the a cant be turned into b 
    
    

        
            
    
            

    
    '''