# Uses python3
import sys

def optimal_summands(n):
    if n<=2:
        return [n]

    summands = []
    #write your code here
    k = int(((1+8*n)**0.5-1)/2)
    #print("k=%d"%k)
    sumSoFar=int(k*(k-1)/2)
    summands=list(range(1,max(k,2)))
    summands.append(int(n-sumSoFar))
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x,end=' ')
