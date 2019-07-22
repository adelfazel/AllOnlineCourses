# python3
import random
import sys
from time import sleep

numThreads= random.randint(2,10)
numEntries= random.randint(5000,30000)
testData=[random.randint(1,400) for _ in range(numEntries)]
print(str(numThreads)+" "+str(numEntries))
for e in testData:
    print(str(e),end=" ")
