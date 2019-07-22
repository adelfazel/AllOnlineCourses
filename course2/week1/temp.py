data=[4, -1, 4 ,1 ,1]
for i in range(len(data)):
    print(i,end=" ")

print("")
for d in data:
    print(d,end=" ")

print("")

res=[set() for _ in range(len(data))]

for i,x in enumerate(data):
    #print("i=%d,x=%d"%(i,x))
    if x==-1:
       pass
    else:   #res[i].add(0)
       res[x].add(i)
print(res)       
