def maxNumberOfBalloons(text: str) -> int:
        mapp = {
            'b' : 0,
            'a' : 0,
            'l' : 0,
            'o' : 0,
            'n' : 0,
        }

        for i in range(len(text)):
            if text[i] in mapp:
                mapp[text[i]] += 1
        
        for key in mapp:
            if key == 'l' or key == 'o':
                    mapp[key] = mapp[key] // 2
        minVal = 2000 #random value i know is bigger than than the frequency of all of them
        for key,val in mapp.items():
            minVal = min(minVal,val)
        
        return minVal
    
text = 'balon'
print(maxNumberOfBalloons(text))