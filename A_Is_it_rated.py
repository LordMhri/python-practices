n = int(input())
final_arr = []
for _ in range(n):
    before,after = map(int,input().split())
    
    final_arr.append((before,after))
    if before != after:
        print("rated")
        exit()
    
sorted_final_arr = sorted(final_arr,reverse= True)
if final_arr != sorted_final_arr :
    
    print("unrated")
else:
    print("maybe")
        