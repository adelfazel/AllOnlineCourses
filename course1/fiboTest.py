n= int(input())
previous, current=0,1

print("f s c3 m3")
print("0 0 0 0")
print("1 1 1 1")

sum=1
for _ in range(n - 1):
    previous, current = current, previous + current
    sum+=current
    currentM3=current%3
    #sumM2=sum%2
    sumM3=sum%3

    #print(current),
    #print(sum),
    print(currentM3),
    print(sumM3)



    #print(current),
    #for d in range(2,m):
    #    print(current % d),
    #print(current % m)
