def isPrime(candidate):
    for num in range(3, int(candidate ** 0.5) + 1,2):
        if (candidate % num)==0:
            return False
    return True
candidate=int(input())
if candidate%2==0:
    candidate+=1
else:
    candidate+=2

while True:
    
    if isPrime(candidate):
        print(candidate)
        break
    candidate+=2
