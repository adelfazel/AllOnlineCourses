# python3
a=int(input())
b=int(input())


def gcd(a,b):
    if b==0:
        return a;
    else:
        rem= a % b
        return gcd(b,rem)


print(gcd(a,b))
