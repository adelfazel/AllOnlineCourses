# Uses python3
def calc_fib(n):
    if n==0: return 0

    curr=1
    prev=0

    for i in range(0,n-1):
        prev,curr=curr,curr+prev
    return curr

n = int(input())
print(calc_fib(n))
