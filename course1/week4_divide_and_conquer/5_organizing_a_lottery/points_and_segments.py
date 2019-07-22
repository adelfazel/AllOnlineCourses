# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    if x<=a[0]:
        return 0
    if x>=a[-1]:
        return len(a)
    newMid=-1
    mid= (left+right)//2
    while newMid!=mid:
        mid= (left+right)//2
        if (a[mid])==x:
            while a[mid]==a[mid-1]:
                mid-=1
            return mid
        if x<a[mid]:
            right=mid
        else:
            left=mid
        newMid=   (left+right)//2
    if a[mid]<x:
        return mid
    else:
        return mid-1



def findFirst(sortedlist,elem,offset=0):
    if elem>sortedlist[-1]: return len(sortedlist)
    for idx in range(len(sortedlist)):
        if elem<sortedlist[idx]:
            return idx

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    zipped=zip(starts,ends)
    sortedByStart=sorted(zipped,key=lambda x:x[0])
    #sortedByEnd  =sorted(zipped,key=lambda x:x[1])
    for elem in zipped:
        print(elem)
    for pindx in range(len(points)):
        cnt[pindx]=len(list(filter(lambda x:x[0]<=points[pindx] and x[1]>=points[pindx] ,zipped)))
    return cnt

# def naive_count_segments(starts, ends,points ):
#      cnt = [0] * len(points)
#      for pidx in range(len(points)):
#          for i in range(len(starts)):
#             if points[pidx] >= starts[i] and  points[pidx] <= ends[i] :
#                 cnt[pidx]+=1
#      return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    #input="1 3 -10 10 -100 100 0"

    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
    #    print(x),
        print(x, end=' ')

    # n=1
    # m=4
    # starts=   [-10,1,3]
    # ends   =  [10,3,12]
    # points =  [-100,100,0,2]
    # cnt = fast_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x),
