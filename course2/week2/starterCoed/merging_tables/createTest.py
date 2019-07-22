# python3
import random
import sys
from time import sleep

# num_tables,num_merge=5,5
# num_rows = [1 for _ in range(num_tables)]
num_tables,num_merge=6,4
num_rows = [10,0,5,0,3,3]

print("%d %d"%(num_tables,num_merge))
for row in num_rows:print(row,end=" ")
print()
merge=[]
# merge.append((3,5))
# merge.append((2,4))
# merge.append((1,4))
# merge.append((5,4))
# merge.append((5,3))

merge.append((6,6))
merge.append((6,5))
merge.append((5,4))
merge.append((4,3))


for m in merge: print("%d %d"%(m[0],m[1]))



# numtables= (random.randint(2,10),)
# numEntries= random.randint(5000,30000)
# testData=[random.randint(1,400) for _ in range(numEntries)]
# print(str(numThreads)+" "+str(numEntries))
# for e in testData:
#     print(str(e),end=" ")
