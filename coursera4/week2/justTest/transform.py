import heapq


text = input("Enter text for transform:")
def createRotations(text,i):
    return text[i:]+text[:i]
def createRotaitonsWrapper(text):
    for i in range(len(text)):
        yield createRotations(text,i)
res = []
for r in createRotaitonsWrapper(text):
    heapq.heappush(res, r)
print("")
bws = []
while res:
    r = heapq.heappop(res)
    print(r)
    bws+=r[-1]
print("") 
print(''.join(bws))
