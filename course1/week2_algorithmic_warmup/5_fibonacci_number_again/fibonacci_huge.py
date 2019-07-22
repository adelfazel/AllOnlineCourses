# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    previous = 0
    current  = 1
    piesso=-1
    fib={}
    fib[0]=0
    fib[1]=1

    for idx in range(2,n+1):
        previous, current =current, (previous + current)%m
        #fib[idx]=current
        #print("        %d"%current)
        if (previous==1 and current==0):
            piesso=idx
            print("piesso=%d"%idx)
            break

    if piesso==-1:
        return current % m
    else:
        return(fib[n%piesso])


if __name__ == '__main__':
    #input = sys.stdin.read();
    #n, m = map(int, input.split())
    n=int(input())
    m=int(input())

    print(get_fibonacci_huge_naive(n, m))
