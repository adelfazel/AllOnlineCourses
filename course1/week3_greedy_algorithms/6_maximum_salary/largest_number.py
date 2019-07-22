#Uses python3
import sys

def compDigit(a,b):
    if int(a)>int(b):
        return 1
    elif int(a)<int(b):
        return -1
    else: return 0


def cmpfunc(a,b):
    idx=0
    if a==b: return True
    while idx<len(a) and idx<len(b):
        res= compDigit(a[idx],b[idx])
        if res!=0: return res
        idx+=1
    lastIdx=idx-1
    if len(a)>len(b):
        res= compDigit(a[idx],b[lastIdx])
        if res!=0: return res
        idx+=1
    else:
        res= compDigit(a[lastIdx],b[idx])
        if res!=0: return res
        idx+=1
    return len(a)>len(b)

def largest_number(a):
    #write your code here
    res = ""
    a.sort(key=functools.cmp_to_key(cmpfunc),reverse=True)
    print(a)
    for x in a:
        res += x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
