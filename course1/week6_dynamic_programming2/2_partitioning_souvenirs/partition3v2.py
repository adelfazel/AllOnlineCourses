# Uses python3
import sys
import itertools


# def backTrackSol(dynamicMat,items,startPos):
#     Sol=[False] * len(items)
#     capIndex=startPos[0]
#     itemIndx=startPos[1]
#     while itemIndx>0:
#         while dynamicMat[capIndex][itemIndx]==dynamicMat[capIndex][itemIndx-1] and itemIndx>0:
#             itemIndx-=1
#         Sol[itemIndx]=True
#         capIndex-=items[itemIndx]
#         itemIndx-=1
#
#     if capIndex!=0:
#         Sol[0]=True
#
#     return Sol


def findItemsWithCap(capacity, items):
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
    print('\n'.join([' '.join(['{:n}'.format(item) for item in row])
      for row in dynamicMat]))
    return dynamicMat

def checkPriliminaries(A):
    S=sum(A)
    target=S//3
    if ((S % 3)!=0):
        return False
    elif len(A)<3:
        return False
    else:
        containsLarge=False
        for e in A:
            if e > target :
                containsLarge=True
                return False
        return True

def partition3update(A):
    findItemsWithCap(sum(A),A)

if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *A = list(map(int, input.split()))
    #A=[17,59,34,57,17,23,67,1,18,2,59]
    A=[1,1,1]
    #A=[3,3,3,3]
    #A=sorted(A,reverse=True)

    A = list(filter(lambda x: x!=0,A))
    # A = sorted(A,reverse=True)

    if checkPriliminaries(A) == 0:
        print(0)
    else:
        print(partition3update(A))
