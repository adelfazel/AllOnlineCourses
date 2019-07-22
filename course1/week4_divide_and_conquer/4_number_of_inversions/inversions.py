# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):

    if (right - left)<2:
        return 0
    ave=(left + right) // 2
    number_of_inversions=0
    number_of_inversions+=get_number_of_inversions(a,b,left,ave)
    number_of_inversions+=get_number_of_inversions(a,b,ave,right)
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


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
