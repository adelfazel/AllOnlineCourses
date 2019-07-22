# Uses python3
import sys

def get_majority_element(a, left, right):
    res={}
    if left+1==right:
        return 1
    numRemaining=right
    majority=numRemaining//2+1
    maxSoFar=1
    i=0
    while maxSoFar+numRemaining>=majority:
        #print("max_so_far:{0},numRemaining:{1},majority:{2}".format(maxSoFar,numRemaining,majority))
        #print(str(res.keys()))

        if a[i] in res.keys():
            res[a[i]]+=1
            if maxSoFar<res[a[i]]:
                maxSoFar=res[a[i]]
                if maxSoFar==majority:
                    return 1
        else:
            res[a[i]]=1
        numRemaining-=1
        i+=1
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # n = int(input("n:"))
    # a=[]
    # for _ in range(n):
    #     a.append(int(input()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
