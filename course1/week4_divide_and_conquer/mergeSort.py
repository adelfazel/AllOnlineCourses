a=[2,3,9,2,9,1]

from time import sleep


def mergesortWrapper(a,b):
    def mergesort(a,b,left,right):

        if (right - left)<2:
            return 0
        ave=(left + right) // 2
        number_of_inversions=0
        number_of_inversions+=mergesort(a,b,left,ave)
        number_of_inversions+=mergesort(a,b,ave,right)
        leftCounter,rightCounter=left,ave
        gCounter=0
        while leftCounter < ave and rightCounter < right:
            while a[leftCounter]<=a[rightCounter]:
                b[left+gCounter]=(a[leftCounter])
                leftCounter+=1
                gCounter+=1
                if leftCounter==ave:
                    break
            if leftCounter==ave:
                break
            while a[rightCounter]<a[leftCounter]:
                b[left+gCounter]=a[rightCounter]
                rightCounter+=1
                gCounter+=1
                number_of_inversions+=ave-leftCounter
                if rightCounter==right:
                    break
        for i in range(leftCounter,ave):
            b[left+gCounter]=a[i]
            gCounter+=1
        for i in range(rightCounter,right):
            b[left+gCounter]=a[i]
            gCounter+=1

        a[left:right]=b[left:right]

        return number_of_inversions


    return mergesort(a,b,0,len(a))
b=[0]*len(a)
print(mergesortWrapper(a,b))
print(a)
