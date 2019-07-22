# Uses python3
import sys

def gcd_good(a, b):
    current_gcd = 1
    rem = a % b
    if rem==0:
        return b
    else: return int(gcd_good(b,rem))

def lcm_naive(a, b):
    gcd= gcd_good(a,b)
    return (int(a/gcd)*b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    #a=int(input())
    #b=int(input())

    print(lcm_naive(a, b))
