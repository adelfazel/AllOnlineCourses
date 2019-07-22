# Uses python3
import sys


def get_change(m):
    #write your code here
    res= [0]*max(m+1,5)
    res[1]=1
    res[2]=2
    res[3]=1
    res[4]=1

    for i in range(5,m+1):
        res[i]=min((res[i-1]+1,res[i-3]+1,res[i-4]+1))
    return res[m]
if __name__ == '__main__':
    m = int(sys.stdin.read())
    #m=int(input())
    print(get_change(m))
