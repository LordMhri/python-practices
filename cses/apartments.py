desired,apartments,offset = map(int,input().split())
people_desire = list(map(int,input().split()))
apartment_size = list(map(int,input().split()))

apartment_size.sort()
people_desire.sort()

ans = 0

'''
sort both apartment size and people's desired size

so 30 60 75 -> apartment size
    45 60 60 80 -> desired

    for 45 check if it is in the range 30-x <= 45 <= 30+x it isnt but also check if 45 > 30 +x if so continue because
    the reason this could'nt be a match is because the desired size is bigger than what we've been offered

    for 45 check if it is in the range 60-x <= 45 <= 60 + x it isnt but when checking 45 > 60+x it fails so we can stop checking if 
    that desire can ever be fulflled because it cant since both are sorted and if current_apartment_size + offset is bigger than the desired
    one

    also if a desire is fulfilled then we should remove that apartment from our list because it is already taken

'''

for desire in people_desire:
    for size in apartment_size:
        if desire-offset < size< desire + offset:
            ans += 1
            apartment_size.remove(size)
            break
        else:
            if size + offset > desire:
                break
    
        




print(ans)