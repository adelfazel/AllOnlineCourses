text="aaabbbccddddeeess"
pattern="ass"
PL=len(pattern)
print("Text:",text)
for i in range(len(text) ,max(PL-1,0),-1):
    print(text[i-PL:i])
    
