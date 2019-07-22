
def partition3(a, l, r):
    x = a[l]
    rr=r
    ll=l
    i=ll
    while i<rr:
        if a[i]>x:
            a[i],a[rr]=a[rr],a[i]

        elif a[i]<x:
            a[i],a[ll]=a[ll],a[i]
            i+=1
            ll+=1
        else:
            i+=1




a=[12,12,23,12,5,3,3,5,5,2,23,2,12]
partition3(a,0,len(a))
print(a)
