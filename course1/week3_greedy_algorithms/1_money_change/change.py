# Uses python3
import sys

def get_change(m):
    #write your code here
    L=  m // 10
    m=  m % 10
    M= (m) // 5
    m=  m % 5

    return int(L+M+m)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
