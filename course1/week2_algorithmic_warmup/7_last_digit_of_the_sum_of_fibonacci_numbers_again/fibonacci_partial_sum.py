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
        sum += current % 10
    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    #from_=int(input())
    #to=int(input())

    SumPiesso=fibonacci_sum_naive(Piesso)
    SumPiessoStart=(SumPiesso-fibonacci_sum_naive((from_-1) % Piesso)) % 10
    SumPiessoBlocksTo=(int((to-(from_-1)) / Piesso)*SumPiesso) % 10
    SumPiessoRemainTo=fibonacci_sum_naive(to % Piesso) % 10
    #print("Sum Piesso Block {0} Sum Start {1} Sum Block {2} Sum Rem".format(SumPiesso,
    #SumPiessoStart,SumPiessoBlocksTo,SumPiessoRemainTo))
    resTo=(SumPiessoStart+SumPiessoBlocksTo+SumPiessoRemainTo)%10
    print(resTo)
