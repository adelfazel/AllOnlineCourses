# Uses python3
import sys


def backTrackSol(dynamicMat,items,startPos):
    Sol=[False] * len(items)
    capIndex=startPos[0]
    itemIndx=startPos[1]
    while itemIndx>0:
        while dynamicMat[capIndex][itemIndx]==dynamicMat[capIndex][itemIndx-1] and itemIndx>0:
            itemIndx-=1
        Sol[itemIndx]=True
        capIndex-=items[itemIndx]
        #print("itemIdx:%d capIdx:%d"%(itemIndx,capIndex))
        itemIndx-=1

    if capIndex!=0:
        Sol[0]=True

    return Sol


def optimal_weight(capacity, items):

    items=sorted(items)
    while items[0]<=0:
        del items[0]
    n=int(len(items))

    if n==0:
         return 0
    if capacity<items[0]:
         return 0
    if items[-1]==0:
        return 0
    if n==1:
        return max(items[0],0)
    while capacity<items[-1]:
        del items[-1]

    n=int(len(items))

    # handle the first item and fill the matrix
    dynamicMat= [[0 for _ in range(n)] for _ in range(capacity+1)]
    for capIndex in range(items[0],capacity+1):
        dynamicMat[capIndex][0]=items[0]
        # for each item
    for itemIndex in range(1,n):
        # for capacities smaller than item itself, fill it from previous column
        for capIndex in range(1,items[itemIndex]):
            dynamicMat[capIndex][itemIndex]=dynamicMat[capIndex][itemIndex-1]
        # for capacities equal to the weight of the item and larger
        for capIndex in range(items[itemIndex],capacity+1):
            i1=dynamicMat[capIndex][itemIndex-1] # best solution without this item
            i2=dynamicMat[capIndex-items[itemIndex]][itemIndex-1]+items[itemIndex]
            # best solution with this item
            dynamicMat[capIndex][itemIndex]=   max(i1,i2)


    # print('\n'.join([' '.join(['{:n}'.format(item) for item in row])
    #   for row in dynamicMat]))
    sol=backTrackSol(dynamicMat,items,(capIndex,itemIndex))
    print(sol)
    s=0
    for idx in range(len(sol)):
        if sol[idx]:
            s+=items[idx]
    print("sum of sol:%d"%s)

    return dynamicMat[capacity][n-1]



if __name__ == '__main__':
    # input = sys.stdin.read()
    # W, n, *w = list(map(int, input.split()))
    # W=20
    # w=[-1,0,0,1,11,17,18,12,12,12,13,13,14,16,17,201,12312]
    W=20
    w=[1,3,4,4,5,6,12,17]
    print("optimal val:%d"%optimal_weight(W, w))
