

def normalize(r,add,length):
    r.extend([0]*add)
    x=([0]*(length-len(r)))
    x.extend(r)
    return x

def printobject(objectName,object):
    print(objectName+":"+str(object))

def prepare(x1,x2):
    n = max(len(x1),len(x2))
    x1=normalize(x1,0,n)
    x2=normalize(x2,0,n)
    printobject("x1",x1)
    printobject("x2",x1)
    return x1,x2

def mult(x1,x2):
    n = max(len(x1),len(x2))
    res = [0]*(n*2-2)
    x1,x2=prepare(x1,x2)

    a1=x1[:n/2]
    a0=x1[n/2:]
    print("a1:%s"%str(a1))
    print("a0:%s"%str(a0))
    b1=x2[:n/2]
    b0=x2[n/2:]
    r11=mult2(a1,b1)
    r10=mult2(a1,b0)
    r01=mult2(a0,b1)
    r00=mult2(a0,b0)
    r11=normalize(r11,n,  2*n-2)
    r10=normalize(r10,n/2,2*n-2)
    r01=normalize(r01,n/2,2*n-2)
    r00=normalize(r00,0,  2*n-2)
    print("r11: %s" %str(r11))
    print("r10: %s" %str(r10))
    print("r01: %s" %str(r01))
    print("r00: %s" %str(r00))
    for i in range(2*n-2):
        res[i]=r11[i]+r10[i]+r01[i]+r00[i]
    return res

def mult2(x1,x2):
    res = [0]*(len(x1)+len(x2)-1)
    for i in range(len(x1)):
        for j in range(len(x2)):
            res[i+j]+=x1[i]*x2[j]
    return res

x1=[1,2,1,4]
x2=[12,1,2,3]

print("x1:%s"%str(x1))
print("x2:%s"%str(x2))
print(str(mult(x1,x2)))
