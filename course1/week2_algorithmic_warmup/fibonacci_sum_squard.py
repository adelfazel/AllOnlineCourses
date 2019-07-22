# Uses python3
import sys


Piesso=60

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current % 10
        sum += current**2 % 10

    return sum % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    #n=int(input())
    #if n<=Piesso:
    #resN=(fibonacci_sum_naive(n))
    #else:
    SumPiesso=fibonacci_sum_naive(Piesso)
    SumPiessoBlocks=(int(n / Piesso)*SumPiesso) % 10
    SumPiessoRemain=fibonacci_sum_naive(n % Piesso) % 10
    resF=(SumPiessoBlocks+SumPiessoRemain)%10
    #print("Naive {0} Fast {1}".format(resN,resF))
    print(resF)
