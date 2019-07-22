# Uses python3
import sys

def optimal_sequence(n):
    res={}
    res[1]=[1]
    res[2]=[1,2]
    res[3]=[1,3]
    Li=[0]*3
    for i in range(4,n+1):
        res[i]=list();
        Li[0]=len(res[i-1])
        if i % 3 ==0:
            Li[1]=len(res[(i) // 3 ])
        else: Li[1]=i
        if i % 2 ==0:
            Li[2]=len(res[(i) // 2 ])
        else: Li[2]=i
        bestI=Li.index(min(Li))
        if bestI==0:
            res[i].extend(res[i-1])
        elif bestI==1:
            res[i].extend(res[i // 3])
        else:
            res[i].extend(res[i // 2])
        res[i].append(i)
    return res[n]


n=int(sys.stdin.read())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x),
